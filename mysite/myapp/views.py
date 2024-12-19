from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
#myapp.models == .models

# Create your views here.

def index(request):
    items = Product.objects.all()
    context = {
        'items':items
    }
    return render(request, "myapp/index.html", context)

def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request, "myapp/details.html", context=context)
    #return HttpResponse("Your item id is: " + str(id))
