from django.shortcuts import render
from django.http import HttpResponse
from .models import machine_data
from .forms import main_appForm
from django.core.paginator import Paginator #ページ制御

def index(request, num=1):
    data = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    page = Paginator(data, 3)
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': main_appForm(),
        'data': [],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = machine_data.objects.get(id=num)
        params['data'] = [item]
        params['form'] = main_appForm(request.POST)
    else:
        #ページ制御
        data = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
        page = Paginator(data,7)
        params['data'] = page.get_page(num)
    
    return render(request, 'main_app/index.html', params)
#****************************************************************

"""
def exel_export(request, num):
    data = machine_data.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': main_appForm(),
        'data': [],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = machine_data.objects.get(id=num)
        params['data'] = [item]
        params['form'] = main_appForm(request.POST)
    else:
        #ページ制御
        data = machine_data.objects.all()
        page = Paginator(data,7)
        params['data'] = page.get_page(num)
    
    return render(request, 'main_app/index.html', params)
"""
# Create your views here.
