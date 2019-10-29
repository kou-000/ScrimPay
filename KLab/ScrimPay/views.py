from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Main, User, Service
import json
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
# import logging
# Create your views here.

# logger=logging.getLogger(__name__)​​

class ItemCreateView(TemplateView):

    template_name = 'ScrimPay/index.html'
    model = Main
    # print("test")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['val3'] = Service.objects.all()
        context['test'] = 'sample'
        return context
    
    # def get_context2_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context['val'] = Main.objects.all().filter(user_id='A001')
    #     return context


    def post(self, request, *args, **kwargs):
        # print("debug")
        some_var = request.POST.getlist('checks[]')
        # print(str(some_var))
        number = len(some_var)
        # print(str(number))
        data = Service.objects.all()

        # sum = 0
        # # #合計金額計算
        # for w in some_var:
        #     sum = int(data[int(w)-1].fee_per_month) + sum
        
        # # #合計金額出力
        # print("sum = "+str(sum))


        # # #各サービスの占める割合の算出
        # service_rate_list = []
        # service_id_list = []
        # for w in some_var:
        #     print(data[int(w)-1].service_id + " : " + str(int(data[int(w)-1].fee_per_month)/sum*100) + "%")
        #     service_rate_list = service_rate_list + [int(data[int(w)-1].fee_per_month)/sum*100]
        #     service_id_list = service_id_list + [str(data[int(w)-1].service_id)]

        #引数としてuser_id(A001)があった場合

        for w in some_var:
            # main_data = Main(user_id = 'A001',service_id = str(data[int(w)-1].service_id))
            main_data = Main(user_id = 'A001',service_id = str(w))
            # print(main_data.user_id)
            # print(main_data.service_id)
            main_data.save()
            # print(w)
        
        return redirect(to='/scrimpay/main')

        # calc_dic = {
        #     'sum':sum,
        #     'service_rate_array':service_rate_list,
        #     'service_id_array':service_id_list,
        # }
        # print(service_rate_list)
        # print(service_id_list)
        # return render(request,'scrimpay/main.html',calc_dic)



def index(request):
    data1 = Main.objects.all()
    data2 = User.objects.all()
    data3 = Service.objects.all()

    value = 0
   
    my_dict = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'v':value,
    }    

    return render(request,'scrimpay/index.html',my_dict)


# def test(self, request, *args, **kwargs):
#     some_var = request.POST.getlist('checks[]')
#         # print(str(some_var))
#         # number = len(some_var)
#     #     model = Main
#     #     data = Service.objects.all()
#     # for w in some_var:
#     #         main_data = Main(user_id = 'A001',service_id = str(data[int(w)-1].service_id))
#     #         print(main_data.user_id)
#     #         print(main_data.service_id)
#     #         main_data.save()
        
#     return redirect(to='/scrimpay/main')


def main(request):
    data1 = Main.objects.all().filter(user_id='A001')
    data2 = User.objects.all().filter(user_id='A001')
    data3 = Service.objects.order_by('-fee_per_month')
    # data3 = Service.objects.order_by('fee_per_month').first()

    print(data3)

    array = []
    for i in data3:
        for j in data1:
            if i.service_id == j.service_id:
                array.append(i.service_name)

    fee_sum = 0
    for i in data3:
        for j in data1:
            if i.service_id == j.service_id:
                fee_sum = fee_sum + i.fee_per_month

    rate_array = []
    for i in data3:
        for j in data1:
            if i.service_id == j.service_id:
                rate = round(i.fee_per_month/fee_sum, 2)
                rate_array.append(rate)

    color_array = []
    for i in data3:
        for j in data1:
            if i.service_id == j.service_id:
                color_array.append(i.color)

    my_dict2 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'array':array,
        'fee_sum':fee_sum,
        'rate_array':rate_array,
        'color_array':color_array,
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