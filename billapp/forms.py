from django import forms
from .models import billone,part
class plistforms(forms.Form):
    prod = forms.CharField(label='prod', max_length=100000)
    qty = forms.CharField(label='qty',max_length=100)
    rate = forms.CharField(label='rate', max_length=100)


class billforms(forms.ModelForm):
    class Meta:
        model = billone
        fields = ['oneprod', 'oneqty','onepra', 'onerate']
        labels = {
            'oneprod': 'Product Name',
            'oneqty': 'Quantity',
            'onepra': 'prize of one pcie',
            'onerate': 'Rate',
        }

class partform(forms.ModelForm):
    class Meta:
        model = part
        fields = ['product','qty','rate','toqrate','peccen','come','totalfee']
        labels = {
            'product':'Product',
            'qty':'Qty',
            'rate':'prize of the pcie',
            'peccen':'percentage',
            'come':'Referral ',
            'totalfee':'Final Prize',
            'toqrate':'prize'
        }
class billperforms(forms.Form):
    prod = forms.CharField(label='prod', max_length=1500)
    qty =  forms.CharField(label='qty', max_length=1000)
    rate = forms.CharField(label='rate', max_length=1000)
    