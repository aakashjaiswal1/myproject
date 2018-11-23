from .forms import NameForm
from django.shortcuts import render
# from django.core.context_processors import csrf
# Create your views here.
from django.http import HttpResponse
from myapp.models import Ebom
from myapp.models import Product
def index(request):
    product_list=Product.objects.all()
    dict2={}
    for item in product_list:
        dict2[item]=item.price

    my_dict={'insert_me':"hello i am from views.py!"}
    my_dict['acd']=dict2
    return render(request, 'firstapp/index.html', context=my_dict)

def home(request):
    return render(request,'firstapp/home.html')

def submit(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print("inside submit")

            Ebom = form.cleaned_data['Ebom']
            products = []
            for product in Product.objects.all():
                if(Ebom == product.ebom.ebom_name):
                    products.append(product.product_name)

            return render(request,'firstapp/Ebom.html',context={'product':products})

