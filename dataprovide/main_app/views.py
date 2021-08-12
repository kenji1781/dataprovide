from django.shortcuts import render
from django.http import HttpResponse
from .models import machine_data
from .forms import main_appForm
from django.core.paginator import Paginator #ページ制御

def index(request, num=1):
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
#urls.pyのpathにある関数が実行する
def index(request,pnum=1):
    
    #htmlファイル側に使われている変数title,msg等の変数を設定
    #paramsに辞書形式で設定し、renderで返す。
    params = {
        'title':'Data Provide System',
        'msg':  'データープロバイドシステム',
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
        params['data'] = page.get_page(pnum)

    #renderの罤２引数にてどのhtmlファイルを読み出すか指定している
    return render(request,'main_app/index.html',params)


#urls.pyのpathにある関数が実行する
def next(request):
    #htmlファイル側に使われている変数title,msg,gotoの変数を設定
    #paramsに辞書形式で設定し、renderで返す。
    params = {
        'title':'Inamoto Dataprovide',
        'msg':  'アイナックス稲本（株）データープロバイドシステム',
        'goto': 'index',
    }
     #renderの罤２引数にてどのhtmlファイルを読み出すか指定している
    return render(request,'main_app/index.html',params)
"""
# Create your views here.
