from django import forms

class main_appForm(forms.Form):
    #id = forms.IntegerField(label='ID')
    machi = forms.CharField(label='機種') #,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    unit = forms.IntegerField(label='号機')
    #course = forms.IntegerField(label='コースNo.')
    year = forms.IntegerField(label='年')
    month = forms.IntegerField(label='月')
    day = forms.IntegerField(label='日')