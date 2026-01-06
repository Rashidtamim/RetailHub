
from django.shortcuts import render





def get_product(request , slug):
   
        return render(request  , 'product/product.html' )

 