from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>', views.group_list, name='group_list')
]