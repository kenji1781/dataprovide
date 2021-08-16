from django.shortcuts import render
from django.http import HttpResponse
from .models import machine_data #データベースモデル
from .forms import main_appForm #フォーム
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger #ページ制御

def index(request, num=1):
    data = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    page = Paginator(data, 7)
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': main_appForm(),
        'data': [],
    }
    """
    if (request.method == 'POST'):
        num = request.POST['id']
        item = machine_data.objects.get(id=num)
        params['data'] = [item]
        params['form'] = main_appForm(request.POST)
    else:
    """
        #ページ制御
    data = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    page = Paginator(data,7)
    params['data'] = page.get_page(num)
    
    return render(request, 'main_app/index.html', params)
#****************************************************************
def find(request, num=1):
    

    find = []
    data = []
    #find = machine_data.objects.all().order_by('machine_name','unit_no','-date_y','date_m','date_d')
    #paginator = Paginator(find, 7)
    #data = page.get_page(num)

    if(request.method == 'POST'):
        form = main_appForm(request.POST) #入力した内容表示の為
        #**********フォームmachine**********
        m = request.POST['machi']
        #find = machine_data.objects.filter(machine_name=m)

        #**********フォームunit**********
        u = request.POST['unit']
        #find = find.objects.filter(unit_no=u)
        #**********フォームcourse**********
        course = request.POST['course']
        #find = find.objects.filter(unit_no=u)
        #**********フォームyear検索**********
        year = request.POST['year']
        #find = find.objects.filter(date_y=y)
        #**********フォームmonth検索**********
        month = request.POST['month']
        #find = find.objects.filter(date_m=m)
        #**********フォームday検索**********
        day = request.POST['day']
        #find = find.objects.filter(date_d=d)
        #find = machine_data.objects.filter(machine_name=m).filter(unit_no=u).filter(date_y=year).filter(date_m=month).filter(date_d=day)
        find = machine_data.objects.filter(machine_name=m,unit_no=u,course_no=course,date_y=year,date_m=month,date_d=day)
        #**********ページ制御**********
        
        
    else:
        form = main_appForm()
        find = machine_data.objects.all().order_by('machine_name','unit_no','course_no','-date_y','date_m','date_d')
    
    
    paginator = Paginator(find, 7)
    #num = request.GET.get('page',1)
    try:
        data = paginator.page(num)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(1)

    
    params = {
        'title': 'DataProvideSystem',
        'msg':'データプロバイドシステム',
        'form': main_appForm(),
        'data': data,
        }

 

    return render(request, 'main_app/find.html', params)


# Create your views here.
