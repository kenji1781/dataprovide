from django import forms

class main_appForm(forms.Form):
    id = forms.IntegerField(label='ID')