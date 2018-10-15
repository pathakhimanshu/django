from django.conf.urls import url
from appone import views
from django.urls import path

app_name = 'appone'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
