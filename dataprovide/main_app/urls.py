from django.urls import path
from . import views
"""
path('',views.index,name='index'),でプロジェクトurls.py側にて設定されているurlのみで
実行するviews関数を指定している。''←この部分がプロジェクトurls.pyのurlから足される部分。
"""
urlpatterns = [
    path('',views.index,name='index'),
    path('form',views.form,name='form'),
]