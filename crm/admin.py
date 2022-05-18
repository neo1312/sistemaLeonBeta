from django.contrib import admin
from crm.models import Client,Sale,saleItem
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class clientResource(resources.ModelResource):
    class Meta:
        model = Client

class clientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('id',)
    list_filter=()
    resource_class=clientResource
    list_display=('id','name','tipo','phoneNumber')

admin.site.register(Client,clientAdmin)

class saleResource(resources.ModelResource):
    class Meta:
        model = Sale

class saleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('id',)
    list_filter=('client','tipo')
    resource_class=saleResource
    list_display=('id','client','tipo')

admin.site.register(Sale,saleAdmin)

class saleItemResource(resources.ModelResource):
    class Meta:
        model = saleItem

class saleItemAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('id',)
    list_filter=('sale',)
    resource_class=saleItemResource
    list_display=('id','sale','product')

admin.site.register(saleItem,saleItemAdmin)

