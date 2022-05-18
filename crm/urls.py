#basic libraries
from django.urls import path

#import 
from crm.views.client.views import clientList, clientCreate,clientEdit,clientDelete
from crm.views.sale.views import saleList, saleInicia,saleEdit,saleDelete,saleCreate,saleGetData,saleItemView,saleItemDelete,pdfPrint
from crm.views.devolution.views import devolutionList


app_name='crm'
urlpatterns=[
        path('client/list',clientList,name='clientList'),
        path('client/create',clientCreate,name='clientCreate'),
        path('client/edit/<int:pk>/',clientEdit, name='clientEdit'),
        path('client/delete/<int:pk>/',clientDelete,name='clientDelete'),

        path('sale/list',saleList,name='saleList'),
        path('sale/create',saleCreate,name='saleCreate'),
        path('sale/inicia',saleInicia,name='saleInicia'),
        path('sale/getdata',saleGetData,name='saleGetData'),
        path('sale/edit/<int:pk>/',saleEdit, name='saleEdit'),
        path('sale/delete/<int:pk>/',saleDelete,name='saleDelete'),

        path('sale/itemview',saleItemView,name='saleItemView'),
        path('sale/itemdelete/<int:pk>/',saleItemDelete,name='saleItemDelete'),
        path('sale/pdfprint/<int:pk>/',pdfPrint,name='pdfPrint'),

        path('devolution/list',devolutionList,name='devolutionList'),
        ]
