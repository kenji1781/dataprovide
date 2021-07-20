from django.shortcuts import render
from django.http import HttpResponse
from .models import machine_data

#urls.pyのpathにある関数が実行する
def index(request):
    #データベースを全て読み出す。
    data = machine_data.objects.all()

    #htmlファイル側に使われている変数title,msg,gotoの変数を設定
    #paramsに辞書形式で設定し、renderで返す。
    params = {
        'title':'Inamoto Dataprovide',
        'msg':  'アイナックス稲本（株）データープロバイドシステム',
        #'goto': 'next',
        'data': data,
    }
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
