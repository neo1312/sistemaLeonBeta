from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import datetime
from crm.models import Sale
from functools import reduce
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reportSale(request):
    context={
            'url_js':'/static/lib/java/report/reportSale.js',
            }
    return render(request, 'sale.html',context)

@csrf_exempt
def getData(request):
    if request.method == 'POST':
        call=json.loads(request.body)
        date=call['date']
        day=datetime.datetime.strptime(date,"%Y-%m-%d")
        todo=Sale.objects.all()
        filtro=list(filter(lambda x:x.date_created.date()==day.date(),todo))
        ventas=list(map(lambda x:x.get_cart_total,filtro))
        ventas_cost=list(map(lambda x:x.get_cart_total_cost,filtro))
        total_venta=reduce(lambda x,y:x+y,ventas)
        total_venta_c=reduce(lambda x,y:x+y,ventas_cost)
        print(total_venta)
        print(total_venta_c)
        return JsonResponse({'date':date},safe=False)

