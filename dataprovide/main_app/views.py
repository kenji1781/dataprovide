from django.shortcuts import render
from django.http import HttpResponse
from .models import machine_data
from .forms import main_appForm

#urls.pyのpathにある関数が実行する
def index(request):
    

    #htmlファイル側に使われている変数title,msg等の変数を設定
    #paramsに辞書形式で設定し、renderで返す。
    params = {
        'title':'Inamoto Dataprovide',
        'msg':  'アイナックス稲本（株）データープロバイドシステム',
        'form': main_appForm(),
        'data': [],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = machine_data.objects.get(id=num)
        params['data'] = [item]
        params['form'] = main_appForm(request.POST)
    else:
        #データベースを全て読み出す。
        params['data'] = machine_data.objects.all()


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

# Create your views here.
