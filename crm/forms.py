from django.forms import ModelForm
from crm.models import Client,Sale

class clientForm(ModelForm):
    class Meta:
        model = Client 
        fields = '__all__'

class saleForm(ModelForm):
    class Meta:
        model = Sale 
        fields = '__all__'
