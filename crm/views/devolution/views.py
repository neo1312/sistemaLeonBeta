#basic libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse,HttpResponse
import json
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt

#import 

def devolutionList(request):
    data = {
            }
    return render(request, 'devolution/list.html', data)

