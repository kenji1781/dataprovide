from django.shortcuts import render
from django.http import HttpResponse
from .models import machine_data #データベースモデル
from .forms import dateForm, main_appForm #フォーム
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger #ページ制御
import datetime
from openpyxl import workbook,load_workbook


def index(request, num=1):
    find = []
    datechk = []
   
    #form = main_appForm()
    datechk = machine_data.objects.all() #.order_by('machine_name','unit_no','-date_y','date_m','date_d')
    
    for chk in datechk:
        if chk.date_ymd == None:
            year_i  = int(chk.date_y)
            month_i = int(chk.date_m)
            day_i = int(chk.date_d)
            chk.date_ymd = datetime.date(year_i,month_i,day_i)
            chk.save()
    
    find = machine_data.objects.all().order_by('-date_ymd','machine_name','unit_no','course_no')
    #find = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    paginator = Paginator(find, 7)
    

    try:
        data = paginator.page(num)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(1)
        
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': dateForm(),
        'data': data,
        }

    return render(request, 'main_app/index.html', params)

#****************************************************************
def find(request, num=1):
    find = []
    data = []
   
    if(request.method == 'POST'):
        #obj = machine_data()
        #input_data = dateForm(request.POST,instance=obj)
        m_n = request.POST['machine_name']
        u_n = request.POST["unit_no"]
        d_m = request.POST["date_ymd"]
        
        unit_req = u_n.split() #ユニット№書いた分だけ検索

        d_m = datetime.datetime.strptime(d_m,'%Y-%m-%d')
        print(d_m)
        start_date = d_m - datetime.timedelta(days=7)
        print(start_date)

        d_m = datetime.datetime.date(d_m)
        start_date = datetime.datetime.date(start_date)
        d_m = d_m.strftime('%Y-%m-%d')
        start_date = start_date.strftime('%Y-%m-%d')
        print(d_m)
        print(type(d_m))
        print(start_date)
        print(type(start_date))

        find = machine_data.objects.filter(machine_name=m_n)\
                                    .filter(unit_no__in=unit_req)\
                                    .filter(date_ymd__range=[start_date,d_m])\
                                    .order_by('-date_ymd','machine_name','unit_no')
                                   
                                    #.order_by('-date_ymd','machine_name','unit_no') #,date_y=year,date_m=month,date_d=day)
        unit_req = [int(s) for s in unit_req]
        print(unit_req)
        n=0
        for j in find: #データ分回す
        #for i in unit_req: #号機分回す
            
            
            
            #for j in find: 
            for i in unit_req: #設定号機分回す 
                
                if i == int(j.unit_no): #号機が同じか？
                    if n == int(j.unit_no): 
                        #print(int(i))
                        m = int(j.drying_time)+h #ユニット№同じ
                        
                        
                    else:
                        m = int(j.drying_time)
                    h=m
                    n=int(j.unit_no)
                    
                    print(i)
                    print(type(i))
                    print(m)   
        """
                    
        #**********エクセル制御**********
                    wb = load_workbook('./test.xlsx')
                    ws = wb.active
                    ws["A1"] = k
                    wb.save('test1.xlsx')
                else:
                    k=0
        """ 
               
            


        #**********ページ制御**********
    
    else:
        #form = main_appForm()
        find = machine_data.objects.all().order_by('-date_ymd''machine_name','unit_no')
    paginator = Paginator(find, 7)

    try:
        data = paginator.page(num)
        

    except PageNotAnInteger:
        data = paginator.page(1)
       
    except EmptyPage:
        data = paginator.page(1)
       
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

            if date != i.date_ymd:
                i.date_ymd = date
                i.save() 


    except PageNotAnInteger:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_ymd:
                i.date_ymd = date
                i.save() 

    except EmptyPage:
        data = paginator.page(1)
        for i in data:
            year  = int(i.date_y)
            month = int(i.date_m)
            day = int(i.date_d)
            date = datetime.date(year,month,day)

            if date != i.date_ymd:
                i.date_ymd = date
                i.save() 
    
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': dateForm(),
        'data': data,
        }

    return render(request, 'main_app/find.html', params)
# Create your views here.
