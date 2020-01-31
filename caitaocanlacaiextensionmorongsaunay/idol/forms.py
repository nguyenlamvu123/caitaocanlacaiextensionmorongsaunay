from django import forms

class IdolSearchForm(forms.Form):
##   name = forms.CharField('label'='Name', max_length=200, required=False,
##                          widget=forms.TextInput(
##                             attrs={'class': 'form-horizontal', 'placeholder': 'Name',}))
   name = forms.CharField(label='Name', max_length=200, required=False,
                          widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': 'Name',}))
