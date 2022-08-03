from Django1 import views
from django.urls import path

urlpatterns =[
    path('',views.first,name='first'),
    path('a',views.second,name='second'),
    path('b',views.third,name='third'),
    path('c',views.fourth,name='fourth'),
    path('temp1',views.temp1,name='temp1'),
    path('dtl',views.dtl,name='dtl'),
    path('ForAndIFLoop',views.ForAndIFLoop,name='ForAndIFLoop'),
    path('HTML4',views.HTMLfour,name='HTMLfour'),
    path('HTML5',views.HTMLfive,name='HTMLfive'),
] 