from django import forms
import django
from django.forms import fields, widgets
from .models import machine_data

class main_appForm(forms.Form):
    #id = forms.IntegerField(label='ID')
    machi = forms.CharField(label='機種')#,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    unit = forms.CharField(label='号機')
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
        fields = ['machine_name','unit_no','input_date']
        widgets = {
            'input_date':DateInput(),
        }
        labels = {  'machine_name':'機種',
                    'unit_no':'号機',
                    'input_date':'日付',
                    }


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                self.field["machine_name"].widget.attrs["class"] = "form-control"
                self.field["unit_no"].widget.attrs["class"] = "form-control"
                self.field["input_date"].widget.attrs["class"] = "form-control"
           