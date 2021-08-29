from django.shortcuts import render
from django.http import HttpResponse
from .models import machine_data #データベースモデル
from .forms import dateForm, main_appForm #フォーム
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger #ページ制御
import datetime

def index(request, num=1):
    find = []
    data = []
   
    if(request.method == 'POST'):
        form = main_appForm(request.POST) #入力した内容表示の為
        #**********フォームmachine**********
        m = request.POST['machi']
        #**********フォームunit**********
        u = request.POST['unit']
        #**********フォームcourse**********
        #course = request.POST['course']
        #**********フォームyear検索**********
        #year = request.POST['year']
        #**********フォームmonth検索**********
        #month = request.POST['month']
        #**********フォームday検索**********
        #day = request.POST['day']
        find = machine_data.objects.filter(machine_name=m,unit_no=u)
        #find = machine_data.objects.filter(machine_name=m,unit_no=u,date_y=year,date_m=month,date_d=day)
        #**********ページ制御**********
    else:
        form = main_appForm()
        find = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    paginator = Paginator(find, 7)
    

    try:
        data = paginator.page(num)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                print(year,month,day)
                print(date)
                i.date_machine = date
                i.save() 
            

    except PageNotAnInteger:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                print(year,month,day)
                print(date)
                i.date_machine = date
                i.save() 


    except EmptyPage:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                print(year,month,day)
                print(date)
                i.date_machine = date
                i.save() 

    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': main_appForm(),
        'data': data,
        }

    return render(request, 'main_app/index.html', params)
#****************************************************************
def find(request, num=1):
    find = []
    data = []
   
    if(request.method == 'POST'):
        form = main_appForm(request.POST) #入力した内容表示の為
        #**********フォームmachine**********
        m = request.POST['machi']
        #**********フォームunit**********
        u = request.POST['unit']
        #ユニット№書いた分だけ検索
        unit_req = u.split()


        print(unit_req)
        find = machine_data.objects.filter(machine_name=m)\
                                    .filter(unit_no__in=unit_req)\
                                    .order_by('machine_name','unit_no','-date_y','date_m','date_d') #,date_y=year,date_m=month,date_d=day)
        #**********ページ制御**********
    else:
        form = main_appForm()
        find = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    paginator = Paginator(find, 7)

    try:
        data = paginator.page(num)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                i.date_machine = date
                i.save() 


    except PageNotAnInteger:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                i.date_machine = date
                i.save() 

    except EmptyPage:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                i.date_machine = date
                i.save() 
    
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': dateForm(),
        'data': data,
        }

    return render(request, 'main_app/find.html', params)

#****************************************************************
def date(request, num=1):
    find = []
    data = []
   
    if(request.method == 'POST'):
        form = main_appForm(request.POST) #入力した内容表示の為
        #**********フォームmachine**********
        m = request.POST['machi']
        #**********フォームunit**********
        u = request.POST['unit']
        #**********フォームcourse**********
        #course = request.POST['course']
        #**********フォームyear検索**********
        #year = request.POST['year']
        #**********フォームmonth検索**********
        #month = request.POST['month']
        #**********フォームday検索**********
        #day = request.POST['day']
        find = machine_data.objects.filter(machine_name=m,unit_no=u)\
                                    .order_by('machine_name','unit_no','-date_y','date_m','date_d')
        #**********ページ制御**********
    else:
        form = main_appForm()
        find = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    paginator = Paginator(find, 7)

    try:
        data = paginator.page(num)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                i.date_machine = date
                i.save() 


    except PageNotAnInteger:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                i.date_machine = date
                i.save() 

    except EmptyPage:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_machine:
                i.date_machine = date
                i.save() 
    
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': dateForm(),
        'data': data,
        }

    return render(request, 'main_app/find.html', params)
# Create your views here.
