from django import forms

class FormSimulateur2017(forms.Form):
    abs_NDA = forms.IntegerField(initial=0,max_value=100,min_value=0,label="Abstention des votants pour NDA (%)")
    mac_NDA = forms.IntegerField(initial=0,max_value=100,min_value=0,label="Votes se reportant sur Macron (%)")
   