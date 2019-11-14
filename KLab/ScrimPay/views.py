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


    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('checks[]')
        number = len(some_var)
        data = Service.objects.all()

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


def main(request):
    data1 = Main.objects.all().filter(user_id='A001')
    data2 = User.objects.all().filter(user_id='A001')
    data3 = Service.objects.order_by('-fee_per_month')

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
   
def SearchCriteria(request):
    return render(request,'ScrimPay/search.html')

def rod(request):
    data1 = Main.objects.all().filter(user_id='A001')
    data2 = User.objects.all().filter(user_id='A001')
    data3 = Service.objects.order_by('-fee_per_month')
    # data3 = Service.objects.order_by('fee_per_month').first()

    if request.method =='POST':
        if 'reverse' in request.POST:
            print('pressed 戻る')
            return redirect('/scrimpay/main')

        elif 'move' in request.POST:
            print('pressed 検索')
            some_var = request.POST.getlist('checks[]')
            tag1 = request.POST.getlist('tag1')
            tag2 = request.POST.getlist('tag2')
            tag3 = request.POST.getlist('tag3')
            budget1 = request.POST.getlist('budget1')
            budget2 = request.POST.getlist('budget2')

            if int(budget1[0]) > int(budget2[0]):
                tmp = budget1[0]
                budget1[0] = budget2[0]
                budget2[0] = tmp

            elif int(budget1[0]) == int(budget2[0]):
                return redirect('/scrimpay/search')

            print(str(some_var))
            print(str(tag1))
            print(str(tag2))
            print(str(tag3))
            print(str(budget1))
            print(str(budget2))

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

    # calcuration
    # search画面で入力した条件を元に複数のplanの組み合わせを作成
    # 出力は、plan1,plan2,plan3の複数
    # plan1 = i.service_name のような形で複数入ってる

    plan1 = ["C001","C006","C016"]
    plan2 = ["C002","C007","C011"]
    plan3 = ["C005","C020","C021","C026"]
    plan_sum = [fee_sum,1000,2000,3000]

    my_dict4 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'array':array,
        'rate_array':rate_array,
        'color_array':color_array,
        'plan1':plan1,
        'plan2':plan2,
        'plan3':plan3,
        'plan_sum':plan_sum
    }             


    return render(request, 'scrimpay/rod.html',my_dict4) 