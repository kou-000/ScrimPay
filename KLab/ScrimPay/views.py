"""

from django.shortcuts import render
from django.urls import reverse_lazy
#from .forms import ItemForm
#from .models import Service
#from .django.views.generic.edit import CreateView
from .models import Select_Service

# Create your views here.

#def post_new(request):
#    form = ItemForm()
#    return render(request, 'blog/post_edit.html', {'form': form})
"""


from django.views.generic.edit import CreateView
from .models import User 
from .models import Service
from .models import Main
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import logging

logger=logging.getLogger(__name__)



class ItemCreateView(TemplateView):
    template_name = 'ScrimPay/index.html'
    model = Main
    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('checks[]')
        print(str(some_var))
        number = len(some_var)

        data = Service.objects.all()
        sum = 0
        for w in some_var:
            #print(w)
            #print(data[int(w)-1].fee_per_month)
            #print(data[int(w)-1])
            sum = int(data[int(w)-1].fee_per_month) + sum
        
        print("sum = "+str(sum))

        for w in some_var:
            print(data[int(w)-1].service_id + " : " + str(int(data[int(w)-1].fee_per_month)/sum*100) + "%")

        #引数としてuser_id(A001)があった場合
        for w in some_var:
            main_data = Main(user_id = 'A001',service_id = str(data[int(w)-1].service_id))
            print(main_data.user_id)
            print(main_data.service_id)
            main_data.save()

        return HttpResponse('')



        

'''
def hello(request):
    data = Service.objects.all()
    d = {
        'val':data,
    }
    return render(request, 'ScrimPay/index.html',d)


def calcmain(request):
    return HttpResponse('<h1>{{some_var}}</h1>')
'''
