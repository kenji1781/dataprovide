from django.shortcuts import render
from django.http import HttpResponse

#urls.pyのpathにある関数が実行する
def index(request):
    #htmlファイル側に使われている変数title,msg,gotoの変数を設定
    #paramsに辞書形式で設定し、renderで返す。
    params = {
        'title':'Inamoto Dataprovide',
        'msg':  'アイナックス稲本（株）データープロバイドシステム',
        #'goto': 'next',
    }
    #renderの罤２引数にてどのhtmlファイルを読み出すか指定している
    return render(request,'main_app/index.html',params)


#urls.pyのpathにある関数が実行する
def form(request):
    msg = request.POST['msg']
    #htmlファイル側に使われている変数title,msg,gotoの変数を設定
    #paramsに辞書形式で設定し、renderで返す。
    params = {
        'title':'Inamoto Dataprovide',
        'msg':  'アイナックス稲本（株）データープロバイドシステム input:'+msg,
        #'goto': 'index',
    }
     #renderの罤２引数にてどのhtmlファイルを読み出すか指定している
    return render(request,'main_app/index.html',params)

# Create your views here.
