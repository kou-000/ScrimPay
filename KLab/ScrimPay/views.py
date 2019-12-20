from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Main, User, Service, Genre
import json
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
import logging
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
    plan1 = Main.objects.all().filter(user_id='A001')
    plan2 = User.objects.all().filter(user_id='A001')
    plan3 = Service.objects.order_by('-fee_per_month')
    # data3 = Service.objects.order_by('fee_per_month').first()

    if request.method =='POST':
        if 'reverse' in request.POST:
            print('pressed 戻る')
            return redirect('/scrimpay/main')

        elif 'button' in request.POST:
            # print('pressed 検索')
            # some_var = []
            # some_var[0] = 
            some_var = request.POST.getlist('checks[]')
            tag1 = request.POST.getlist('tag1')
            tag2 = request.POST.getlist('tag2')
            tag3 = request.POST.getlist('tag3')
            budget1 = request.POST.getlist('budget1')
            budget2 = request.POST.getlist('budget2')
            # slider1 = request.POST.getlist('slider1')
            # slider2 = request.POST.getlist('slider2')
            # slider3 = request.POST.getlist('slider3')
            display = request.POST.getlist('type')

            if int(budget1[0]) > int(budget2[0]):
                tmp = budget1[0]
                budget1[0] = budget2[0]
                budget2[0] = tmp

            elif int(budget1[0]) == int(budget2[0]):
                return redirect('/scrimpay/search')

            # slider1 = int(slider1)
            # slider2 = int(slider2)
            # slider3 = int(slider3)

            # tmp = 'service_id'
            # data_tag1 = Service.objects.values_list(tmp,flat = True)
            

            if str(tag1[0]) == "アニメ":
                tag1[0] = "anime_weight"
            elif str(tag1[0]) == "ドラマ":
                tag1[0] = "drama_weight"
            elif str(tag1[0]) == "邦画":
                tag1[0] = "japanese_movie_weight"
            elif str(tag1[0]) == "スポーツ":
                tag1[0] = "sports_weight"
            elif str(tag1[0]) == "バラエティー":
                tag1[0] = "variety_weight"

            if tag2[0] == "アニメ":
                tag2[0] = "anime_weight"
            elif tag2[0] == "ドラマ":
                tag2[0] = "drama_weight"
            elif tag2[0] == "邦画":
                tag2[0] = "japanese_movie_weight"
            elif tag2[0] == "スポーツ":
                tag2[0] = "sports_weight"
            elif tag2[0] == "バラエティー":
                tag2[0] = "variety_weight" 

            if tag3[0] == "アニメ":
                tag3[0] = "anime_weight"
            elif tag3[0] == "ドラマ":
                tag3[0] = "drama_weight"
            elif tag3[0] == "邦画":
                tag3[0] = "japanese_movie_weight"
            elif tag3[0] == "スポーツ":
                tag3[0] = "sports_weight"
            elif tag3[0] == "バラエティー":
                tag3[0] = "variety_weight"               

            # print(some_var[0])
            if len(some_var) != 0:
                if some_var[0] == "option1" :
                # print("test")
                    identifier = "学割"
                else : 
                    identifier = "一般"
            else:
                identifier = "一般"
            
            # print(identifier)

            
            ##ここから下は使います　あとでコメントアウトを解除しておいてください
            data_tag1 = Genre.objects.values_list(tag1[0],flat = True)
            data_tag2 = Genre.objects.values_list(tag2[0],flat = True)
            data_tag3 = Genre.objects.values_list(tag3[0],flat = True)
            data_id1 = Genre.objects.values_list('service_id',flat = True)
            data_id2 = data_id1
            data_id3 = data_id1
            data_fee1 = Service.objects.values_list('fee_per_month',flat = True)
            data_fee2 = data_fee1
            data_fee3 = data_fee1
            # data_all_service = Service.objects.all()
            # data_identifier = Service.objects.all().filter(plan_identifier=identifier)

            # print(data_all_service)
            # print(data_identifier)
            # sample = []
            # print(len(data_identifier))
            # if identifier == "学割":
                # num = len(data_identifier)
                # for w in range(2,len(data_all_service)):
                    
                    # sample.append(data_all_service[w])
                # print(data_identifier[1])
                # for s in range(len(data_identifier,len(data_all_service)-len(data_identifier))):
                    # for t in range(len(data_identifier))
            # print(sample)
            # data = Service.objects.all()
            # print(data[0])
            
            tag1_sort = []
            tag2_sort = []
            tag3_sort = []
            id1_sort =[]
            id2_sort =[]
            id3_sort =[]
            fee1_sort = []
            fee2_sort = []
            fee3_sort = []

            ##ここから下は使います　あとでコメントアウトを解除しておいてください

            num = len(data_tag1)
            # print(num)
            # print(len(data_fee1))

            ##学割サブスク＋一般サブスクの格納
            if identifier == "学割": 
                tag1_sort.append(data_tag1[2])
                tag2_sort.append(data_tag2[2])
                tag3_sort.append(data_tag3[2])
                id1_sort.append(data_id1[2])
                id2_sort.append(data_id2[2])
                id3_sort.append(data_id3[2])
                fee1_sort.append(data_fee1[2])
                fee2_sort.append(data_fee2[2])
                fee3_sort.append(data_fee3[2])

                for n in range(4,num):
                    tag1_sort.append(data_tag1[n])
                for n in range(4,num):
                    tag2_sort.append(data_tag2[n])
                for n in range(4,num):
                    tag3_sort.append(data_tag3[n])

                for n in range(4,num):
                    id1_sort.append(data_id1[n])
                for n in range(4,num):
                    id2_sort.append(data_id2[n])
                for n in range(4,num):
                    id3_sort.append(data_id3[n])

                for n in range(4,num):
                    fee1_sort.append(data_fee1[n])
                for n in range(4,num):
                    fee2_sort.append(data_fee2[n])
                for n in range(4,num):
                    fee3_sort.append(data_fee3[n])
            
            ##一般サブスクの格納
            else: 
                tag1_sort.append(data_tag1[0])
                tag2_sort.append(data_tag2[0])
                tag3_sort.append(data_tag3[0])
                id1_sort.append(data_id1[0])
                id2_sort.append(data_id2[0])
                id3_sort.append(data_id3[0])
                fee1_sort.append(data_fee1[0])
                fee2_sort.append(data_fee2[0])
                fee3_sort.append(data_fee3[0])


                for n in range(4,num):
                    tag1_sort.append(data_tag1[n])
                for n in range(4,num):
                    tag2_sort.append(data_tag2[n])
                for n in range(4,num):
                    tag3_sort.append(data_tag3[n])

                for n in range(4,num):
                    id1_sort.append(data_id1[n])
                for n in range(4,num):
                    id2_sort.append(data_id2[n])
                for n in range(4,num):
                    id3_sort.append(data_id3[n])

                for n in range(4,num):
                    fee1_sort.append(data_fee1[n])
                for n in range(4,num):
                    fee2_sort.append(data_fee2[n])
                for n in range(4,num):
                    fee3_sort.append(data_fee3[n]) 


            # print(id1_sort)
            # print(id2_sort)
            # print(id3_sort)
            # print(tag1_sort)
            # print(tag2_sort)
            # print(tag3_sort)
            # print(fee1_sort)
            # print(fee2_sort)
            # print(fee3_sort)
            print(len(tag1_sort))

            
            num = len(tag1_sort)
            # print(num)

            for n in range(num-1):
                for j in range(n,num-1):
                    if int(tag1_sort[n]) < int(tag1_sort[j+1]):
                        tmp_tag1 = tag1_sort[j+1]
                        tag1_sort[j+1] = tag1_sort[n]
                        tag1_sort[n] = tmp_tag1

                        tmp_id1 = id1_sort[n]
                        id1_sort[n] = id1_sort[j+1]
                        id1_sort[j+1] = tmp_id1

                        tmp_fee1 = fee1_sort[n]
                        fee1_sort[n] = fee1_sort[j+1]
                        fee1_sort[j+1] = tmp_fee1

            # print(tag1_sort)
            # print(id1_sort)

            for n in range(num-1):
                for j in range(n,num-1):
                    if int(tag2_sort[n]) < int(tag2_sort[j+1]):
                        tmp_tag2 = tag2_sort[j+1]
                        tag2_sort[j+1] = tag2_sort[n]
                        tag2_sort[n] = tmp_tag2

                        tmp_id2 = id2_sort[n]
                        id2_sort[n] = id2_sort[j+1]
                        id2_sort[j+1] = tmp_id2

                        tmp_fee2 = fee2_sort[n]
                        fee2_sort[n] = fee2_sort[j+1]
                        fee2_sort[j+1] = tmp_fee2

            for n in range(num-1):
                for j in range(n,num-1):
                    if int(tag3_sort[n]) < int(tag3_sort[j+1]):
                        tmp_tag3 = tag3_sort[j+1]
                        tag3_sort[j+1] = tag3_sort[n]
                        tag3_sort[n] = tmp_tag3

                        tmp_id3 = id3_sort[n]
                        id3_sort[n] = id3_sort[j+1]
                        id3_sort[j+1] = tmp_id3

                        tmp_fee3 = fee3_sort[n]
                        fee3_sort[n] = fee3_sort[j+1]
                        fee3_sort[j+1] = tmp_fee3

            # print(tag1_sort)
            # print(tag2_sort)
            # print(tag3_sort)

            score = [[0 for i in range(5)] for j in range(num*num*num)]
            
            score_point = []
            score_id1 = []
            score_id2 = []
            score_id3 = []
            score_fee = []
            
            # print(score)
            # print(num)
            # print(len(score))


            y = 0
            for i in range(num):
                for s in range(num):
                    for t in range(num):
                        # score[y][0] = int(tag1_sort[i]) * int(slider1[0]) + int(tag2_sort[s]) * int(slider2[0]) + int(tag3_sort[t]) * int(slider3[0])
                        # score[y][1] = id1_sort[i]
                        # score[y][2] = id1_sort[s]
                        # score[y][3] = id1_sort[t]
                        # score[y][4] = int(fee1_sort[i]) + int(fee2_sort[s]) + int(fee3_sort[t])
                        # y = y + 1
                        score_point.append(int(tag1_sort[i]) * 10 + int(tag2_sort[s]) * 7 + int(tag3_sort[t]) * 3)
                        score_id1.append(id1_sort[i])
                        score_id2.append(id2_sort[s])
                        score_id3.append(id3_sort[t])
                        if id1_sort[i] == id2_sort[s] and id1_sort[i] == id3_sort[t]:
                            score_fee.append(int(fee1_sort[i]))
                        elif id1_sort[i] == id2_sort[s] and id1_sort[i] != id3_sort[t]:
                            score_fee.append(int(fee1_sort[i])+int(fee3_sort[t]))
                        elif id1_sort[i] != id2_sort[s] and id1_sort[i] == id3_sort[t]:
                            score_fee.append(int(fee1_sort[i])+int(fee2_sort[s]))
                        elif id1_sort[i] != id2_sort[s] and id2_sort[s] == id3_sort[t]:
                            score_fee.append(int(fee1_sort[i])+int(fee2_sort[s]))                       
                        else:
                            score_fee.append(int(fee1_sort[i]) + int(fee2_sort[s]) + int(fee3_sort[t]))


            # print(tag1_sort[0])
            # print(int(slider1[0]))
            # print(tag1_sort[0])
            # print(slider1[0])
            # tmp = int(tag1_sort[0]) * int(slider1[0])
            # print(tmp)

            # print(score)
            
            # some_var = request.POST.getlist('checks[]')
            # # print(some_var)
            # print(some_var[0])

            # len_score = len(score)

            # for n in range(len_score-1):
            #     for j in range(n,len_score-1):
            #         if int(score[n][0]) < int(score[j+1][0]):
            #             tmp_score = score[j+1][1]
            #             score[j+1][1] = score[n][1]
            #             score[n][1] = tmp_score
            
            # print(len(score_fee))
            zip_score = zip(score_point,score_id1,score_id2,score_id3,score_fee)
            sort_zip_reverse = sorted(zip_score,reverse=True)
            # print(sort_zip_reverse)
            # print('finish')
            # print(display[0])
            
            score_point,score_id1,score_id2,score_id3,score_fee = zip(*sort_zip_reverse)
            # print(len(score_fee))
            count = 0
            data1 = []
            data2 = []
            data3 = []
            array = []
            sample = []
            tmp_data = []
            # for i in range(int(display[0])):
            for i in range(3):
                for s in range(count,len(score_point)):
                    tmp_data.clear()
                    if i == 0:
                        if int(budget1[0]) <= score_fee[s] and score_fee[s] <= int(budget2[0]):
                            data1.append(score_id1[s])
                            if score_id1[s] != score_id2[s]:
                                data1.append(score_id2[s])
                            if score_id1[s] != score_id3[s] and score_id2[s] != score_id3[s]:
                                data1.append(score_id3[s])
                            array.append(score_fee[s])
                            sample.append(score_point[s])
                            count = count + 1
                            break
                    elif i == 1:
                        tmp_data.append(score_id1[s])
                        if score_id1[s] != score_id2[s]:
                            tmp_data.append(score_id2[s])
                        if score_id1[s] != score_id3[s] and score_id2[s] != score_id3[s]:
                            tmp_data.append(score_id3[s])
                        if sorted(tmp_data) != sorted(data1):
                            tmp_data.clear()
                            if int(budget1[0]) <= score_fee[s] and score_fee[s] <= int(budget2[0]):
                                data2.append(score_id1[s])
                                if score_id1[s] != score_id2[s]:
                                    data2.append(score_id2[s])
                                if score_id1[s] != score_id3[s] and score_id2[s] != score_id3[s]:
                                    data2.append(score_id3[s])
                                array.append(score_fee[s])
                                sample.append(score_point[s])
                                count = count + 1
                                break
                        
                    elif i == 2:
                        tmp_data.append(score_id1[s])
                        if score_id1[s] != score_id2[s]:
                            tmp_data.append(score_id2[s])
                        if score_id1[s] != score_id3[s] and score_id2[s] != score_id3[s]:
                            tmp_data.append(score_id3[s])
                        if sorted(tmp_data) != sorted(data1) and sorted(tmp_data) != sorted(data2):
                            tmp_data.clear()
                            if int(budget1[0]) <= score_fee[s] and score_fee[s] <= int(budget2[0]):
                                data3.append(score_id1[s])
                                if score_id1[s] != score_id2[s]:
                                    data3.append(score_id2[s])
                                if score_id1[s] != score_id3[s] and score_id2[s] != score_id3[s]:
                                    data3.append(score_id3[s])
                                array.append(score_fee[s])
                                sample.append(score_point[s])
                                count = count + 1
                                break
                    count = count + 1




            
            # print(data1)
            # print(data2)
            # print(data3)
            # print(array)
            # print(sample)

            
            # print(str(tag1))
            # print(str(tag2))
            # print(str(tag3))
            # print(str(budget1))
            # print(str(budget2))
            # print(str(slider1))
            # print(str(slider2))
            # print(str(slider3))
            # print(data_tag1)

            # data1 = ["C001","C006","C016"]
            # data2 = ["C002","C007","C011"]
            # data3 = ["C005","C020","C021","C026"]
            # array = [1000,2000,3000]



    # array = []
    # for i in data3:
    #     for j in data1:
    #         if i.service_id == j.service_id:
    #             array.append(i.service_name)

    fee_sum = 0
    for i in plan3:
        for j in plan1:
            if i.service_id == j.service_id:
                fee_sum = fee_sum + i.fee_per_month

    rate_array = []
    for i in plan3:
        for j in plan1:
            if i.service_id == j.service_id:
                rate = round(i.fee_per_month/fee_sum, 2)
                rate_array.append(rate)

    color_array = []
    for i in plan3:
        for j in plan1:
            if i.service_id == j.service_id:
                color_array.append(i.color)

    # calcuration
    # search画面で入力した条件を元に複数のplanの組み合わせを作成
    # 出力は、plan1,plan2,plan3の複数
    # plan1 = i.service_name のような形で複数入ってる

    # plan1_sum = 0
    # for i in data3:
    #     for j in plan1:
    #         if i.service_id == j:
    #             plan1_sum = plan1_sum + i.fee_per_month

    # plan2_sum = 0
    # for i in data3:
    #     for j in plan2:
    #         if i.service_id == j:
    #             plan2_sum = plan2_sum + i.fee_per_month

    # plan3_sum = 0
    # for i in data3:
    #     for j in plan3:
    #         if i.service_id == j:
    #             plan3_sum = plan3_sum + i.fee_per_month

    plan_sum = []
    plan_sum.append(fee_sum)
    # array = []
    print(array)
    for i in range(len(array)):
        plan_sum.append(array[i])

    
    # plan_sum = [fee_sum, plan1_sum, plan2_sum, plan3_sum]

    my_dict4 = {
        'val':plan1,
        'val2':plan2,
        'val3':plan3,
        'array':array,
        'rate_array':rate_array,
        'color_array':color_array,
        'plan1':data1,
        'plan2':data2,
        'plan3':data3,
        'plan_sum':plan_sum
    }             


    return render(request, 'scrimpay/rod.html',my_dict4) 

def support(request):
    data1 = Main.objects.all().filter(user_id='A001')
    data2 = User.objects.all().filter(user_id='A001')
    data3 = Service.objects.order_by('-fee_per_month')
    service_id_for_replace = Service.objects.values_list('service_id',flat=True)

    if request.method =='POST':
        if 'change1' in request.POST:
            plan = request.POST.getlist('pl1[]')
            # print("plan:",plan)

        elif 'change2' in request.POST:
            plan = request.POST.getlist('pl2[]')
            

        elif 'change3' in request.POST:
            plan = request.POST.getlist('pl3[]')
            # print("plan:",plan)

    for n in range(len(plan)):
        for i in service_id_for_replace:
            tmp = "&#x27;"+i+"&#x27;"
            # print(tmp)
            if plan[n] == tmp:
                plan[n] = i

    print(plan)

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
    flag = 0

    sevid = []
    for i in data3:
        for j in data1:
            if i.service_id == j.service_id:
                sevid.append(i.service_id)
                flag = 1

    # 新しく加入するサービスを格納
    addlist = []
    flag = 0
    # print(len(sevid))
    # print("plan:",plan)
    print("array:",array)
    # print("plan:",plan)
    
    if len(sevid) != 0:
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
    else:
        for i in plan:
            addlist.append(i)

    # if flag == 0:
    #     for i in plan:
    #         addlist.append(i)
    # else:
    #     flag = 0
    #     for i in plan:
    #         for j in sevid:
    #             if i == j:
    #                 flag = 0
    #                 break
    #             else:
    #                 flag = 1           
    #         if flag == 1:
    #             addlist.append(i)
    #             flag = 0

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

def signup(request):
    data1 = Main.objects.all()
    data2 = User.objects.all()
    data3 = Service.objects.all()

    value = 0

    my_dict7 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'v':value,
    }    

    return render(request,'scrimpay/signup.html',my_dict7)

def signin(request):
    data1 = Main.objects.all()
    data2 = User.objects.all()
    data3 = Service.objects.all()

    value = 0
   
    my_dict8 = {
        'val':data1,
        'val2':data2,
        'val3':data3,
        'v':value,
    }    

    return render(request,'scrimpay/signin.html',my_dict8)

def top(request):
    return render(request,'scrimpay/top.html')