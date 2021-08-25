from django import forms
import django
from django .contrib .admin .widgets import AdminDateWidget
from django.forms import fields, widgets
from .models import machine_data

class main_appForm(forms.Form):
    #id = forms.IntegerField(label='ID')
    machi = forms.CharField(label='機種')#,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    unit = forms.IntegerField(label='号機')
    #course = forms.IntegerField(label='コースNo.')
    #year = forms.IntegerField(label='年')
    #month = forms.IntegerField(label='月')
    #day = forms.IntegerField(label='日')
    #date_field = forms.DateField(widget=AdminDateWidget())

"""
class dateForm(forms.Form):
    #id = forms.IntegerField(label='ID')
    #machi = forms.CharField(label='機種') #,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    #unit = forms.IntegerField(label='号機')
    #course = forms.IntegerField(label='コースNo.')
    #year = forms.IntegerField(label='年')
    #month = forms.IntegerField(label='月')
    #day = forms.IntegerField(label='日')
    date_machine = forms.DateField(widget=DateInput())
"""



class DateInput(forms.DateInput):
    input_type = 'date'


class dateForm(forms.ModelForm):
    class Meta:
        model = machine_data
        fields = ['date_machine']
        widgets = {
            'date_machine':DateInput(),
        }
        labels = {'date_machine':'日付',}


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                self.field["date_machine"].widget.attrs["class"] = "form-control"
           