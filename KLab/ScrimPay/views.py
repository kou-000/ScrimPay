from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Main, User, Service
import json
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DeleteView
# import logging
# Create your views here.

# logger=logging.getLogger(__name__)​​

class ItemCreateView(TemplateView):

    template_name = 'ScrimPay/index.html'
    model = Main
    # print("test")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_user = Main.objects.all().filter(user_id='A001')
        data_service = Service.objects.all()

        list_unsigned=[]
        for w in data_service:
            flag = 1
            for i in data_user:
                data_name = Service.objects.all().filter(service_id=i.service_id)

                if w.service_name == data_name[0].service_name:
                    flag=0
                    break

            if flag==1:
                list_unsigned = list_unsigned + [w]

        context['val3'] = list_unsigned
        context['test'] = 'sample'
        return context


    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('checks[]')
        print(str(some_var))
        data = Service.objects.all()

        #引数としてuser_id(A001)があった場合

        for w in some_var:
            main_data = Main(user_id = 'A001',service_id = str(w))
            main_data.save()

        return redirect('/scrimpay/main')

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

    if request.method =='POST':
        if 'button' in request.POST:
            some_var = request.POST.getlist('deletes[]')
            print(str(some_var))

            for w in some_var:
                main_data = Main.objects.filter(user_id = 'A001', service_id = str(w))
                main_data.delete()

        elif 'plan_cd' in request.POST:
            add_var = request.POST.getlist('plan_add[]')
            print(str(add_var))
            del_var = request.POST.getlist('plan_del[]')
            print(str(del_var))

            for n in add_var:
                add_data = Main(user_id = 'A001', service_id = str(n))
                add_data.save()

            for k in del_var:
                del_data = Main.objects.filter(user_id = 'A001', service_id = str(k))
                del_data.delete()
            

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
            slider1 = request.POST.getlist('slider1')
            slider2 = request.POST.getlist('slider2')
            slider3 = request.POST.getlist('slider3')

            if int(budget1[0]) > int(budget2[0]):
                tmp = budget1[0]
                budget1[0] = budget2[0]
                budget2[0] = tmp

            elif int(budget1[0]) == int(budget2[0]):
                return redirect('/scrimpay/search')


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

    plan1_sum = 0
    for i in data3:
        for j in plan1:
            if i.service_id == j:
                plan1_sum = plan1_sum + i.fee_per_month

    plan2_sum = 0
    for i in data3:
        for j in plan2:
            if i.service_id == j:
                plan2_sum = plan2_sum + i.fee_per_month

    plan3_sum = 0
    for i in data3:
        for j in plan3:
            if i.service_id == j:
                plan3_sum = plan3_sum + i.fee_per_month

    plan_sum = [fee_sum, plan1_sum, plan2_sum, plan3_sum]

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


def support(request):
    data1 = Main.objects.all().filter(user_id='A001')
    data2 = User.objects.all().filter(user_id='A001')
    data3 = Service.objects.order_by('-fee_per_month')

    if request.method =='POST':
        if 'change1' in request.POST:
            plan = request.POST.getlist('pl1[]')

        elif 'change2' in request.POST:
            plan = request.POST.getlist('pl2[]')

        elif 'change3' in request.POST:
            plan = request.POST.getlist('pl3[]')

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

    # calculate
    # 現在利用しているサービスのID取得
    sevid = []
    for i in data3:
        for j in data1:
            if i.service_id == j.service_id:
                sevid.append(i.service_id)

    # 新しく加入するサービスを格納
    addlist = []
    flag = 0
    for i in plan:
        for j in sevid:
            if i == j:
                flag = 0
                break
            else:
                flag = 1           
        if flag == 1:
            addlist.append(i)
            flag = 0

    # 解約するサービスを格納
    dellist = []
    flag = 0
    for i in sevid:
        for j in plan:
            if i == j:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            dellist.append(i)
            flag = 0

    my_dict5 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'array':array,
        'rate_array':rate_array,
        'color_array':color_array,
        'plan':plan,
        'addlist':addlist,
        'dellist':dellist,
    }             


    return render(request, 'scrimpay/support.html',my_dict5) 

def deletedb(request):
    data1 = Main.objects.all()
    data2 = User.objects.all()
    data3 = Service.objects.all()

    value = 0
   
    my_dict6 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'v':value,
    }    

    return render(request,'scrimpay/deletedb.html',my_dict6)

def top(request):
    return render(request,'scrimpay/top.html')