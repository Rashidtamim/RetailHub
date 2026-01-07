from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

    context = {'products' : Product.objects.all()}
    return render(request , 'home/index.html' , context)

@login_required
def home2(request):

    context = {'products' : Product.objects.all()}
    return render(request , 'home/index1.html' , context)


