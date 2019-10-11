from django.shortcuts import render
from django.http import HttpResponse
from .models import Main, User, Service
import json
# Create your views here.

def index(request):
    my_dict = {
        'insert_something':"views.pyのinsert_something部分です。",
        'name':'Bashi'
    }
    return render(request,'scrimpay/index.html',my_dict)

def main(request):
    data1 = Main.objects.all().filter(user_id='A001')
    data2 = User.objects.all().filter(user_id='A001')
    data3 = Service.objects.all()

    array = []
    for i in data1:
        for j in data3:
            if i.service_id == j.service_id:
                array.append(j.service_name)
    print(array)
    my_dict2 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'array':array,
    }             


    return render(request, 'scrimpay/main.html',my_dict2)    

def detail(request):
    data1 = Main.objects.all().filter(user_id='A001')
    data2 = User.objects.all().filter(user_id='A001')
    data3 = Service.objects.all()

    my_dict3 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
    }
    return render(request, 'scrimpay/detail.html',my_dict3)
