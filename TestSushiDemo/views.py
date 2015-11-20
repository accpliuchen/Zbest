from django.http.response import HttpResponse
from django.shortcuts import render

from django.template.loader import  get_template
from django.template import Context

from TestSushiDemo.dao import getMenu,getProducts
from numpy.f2py.crackfortran import endifpattern

def loadMenu(request):
    result=getMenu()

    return render(request,'index.html',{'resultlist':result})

def product(request):
     
     if 'q' in request.GET:
       message = 'You paremeter is : %r' % request.GET['q']
       id=request.GET['q'];
       result_product=getProducts(id)
       print result_product
       return render(request,'product2.html',{'resultlist':result_product});
     else:
        message = 'Your paremeter is empty'
      
     print message
       
    

def index(request):
   return render(request,'index.html')