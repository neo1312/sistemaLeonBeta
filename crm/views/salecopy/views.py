#basic libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse,HttpResponse
import json
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt

#import 
from crm.models import Sale,Client ,Product,saleItem
from crm.forms import saleForm 

@csrf_exempt
def saleInicia(request):
    if request.method == "POST":
        data=json.loads(request.body)
        tipo=(data[0])
        client=Client.objects.get(name='mostrador')
        sale=Sale.objects.create(client=client,tipo=tipo)
        sale.save()
    return JsonResponse('Venta Registrada',safe=False)

def saleList(request):
    data = {
            'sale_create':'/sale/create',
            'title' : 'Listado sales',
            'sales' : Sale.objects.all(),
            'entity':'sales',
            'url_create':'/sale/create',
            'url_js':'/static/lib/java/sale/list.js',
            'btnId':'btnOrderList',
            }
    return render(request, 'sale/list.html', data)

@csrf_exempt
def saleEdit(request,pk):
    sale=get_object_or_404(Sale,id=pk)
    if request.method != 'POST':
        form=saleForm(instance=sale)
    else:
        form = saleForm(request.POST,instance=sale)
        if form.is_valid():
            form.save()
            return redirect ( '/sale/list')
    context={
            'form':form,
            'title' : 'sale Edit',
            'entity':'salees',
            'retornoLista':'/sale/list',
            } 
    return render(request, 'sale/edit.html',context) 

@csrf_exempt
def saleDelete(request,pk):
    sale=Sale.objects.get(id=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect ( '/sale/list')

    context = {
            'item':sale,
            'title' : 'sale Delete',
            'entity':'salees',
            'retornoLista':'/sale/list',
            }
    return render(request,  'sale/delete.html',context)

def saleCreate(request):
    sale=Sale.objects.last()
    items=sale.saleitem_set.all()
    context={
            'url_js':'/static/lib/java/sale/create.js',
            'items':items,
            'total':sale,
            'returnList':'/sale/list'
            }
    return render(request, 'sale/create.html',context)

@csrf_exempt
def saleGetData(request):
    if request.method == 'POST':
        call= json.loads(request.body)
        pk=call['id']
        qs=Product.objects.get(barcode=pk)
        sale=Sale.objects.last()
        if sale.tipo=='menudeo':
            name = [qs.id,qs.name,qs.priceToday]
        else:
            name = [qs.id,qs.name,qs.priceMayoreo]
        return JsonResponse({'datos':name},safe=False)

@csrf_exempt
def saleItemView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        sale=Sale.objects.last()
        pk=int(data[0])
        quantity=data[1]
        product=Product.objects.get(id=pk)
        if sale.tipo == 'menudeo':
            if product.granel==True:
                if float(quantity) < float(product.minimo):
                    cost=product.priceGranel
                    margen=product.margenGranel
                else:
                    cost=product.priceToday
                    margen=product.margen
            else:
                cost=product.priceToday
                margen=product.margen
        else:
            cost=product.priceMayoreo
            margen=product.margenMayoreo

        stockActual=(Product.objects.get(id=pk)).stock
        if int(quantity) > stockActual:
            return JsonResponse('No hay stock suficiente', safe=False)
        else:
            itemssale=sale.saleitem_set.all()
            outputlist=list(filter(lambda x:x.product.id==pk,itemssale))
            print(stockActual)
            if outputlist:
                repetido=outputlist[0]
                quantity=int(repetido.quantity)+int(quantity)
                saleItem.objects.filter(id=repetido.id).delete()
                saleItem.objects.create(product=product,sale=sale,quantity=quantity,cost=cost,margen=margen)
                return JsonResponse('se sumaron',safe=False)
            else:
                saleItem.objects.create(product=product,sale=sale,quantity=quantity,cost=cost,margen=margen)
                return JsonResponse('creo nuevo registro',safe=False)

@csrf_exempt
def saleItemDelete(request,pk):
    item=saleItem.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect ( '/sale/create')
    context = {
            'item':item,
            'title' : 'item Delete',
            'entity':'orders',
            'retornoLista':'/sale/list',
            }
    return render(request,  'sale/delete.html',context)

@csrf_exempt
def pdfPrint(request,pk):
    sale=Sale.objects.get(id=pk)
    items=sale.saleitem_set.all()
    data={
            "sale":sale,
            "saleId":sale.id,
            "items":items,
            "cliente":sale.client.name
            }
    template_path = 'sale/pdfprint.html'
    context = data
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sale.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
