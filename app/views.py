from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .signals import rahul_signal

# Create your views here.
@csrf_exempt
def Create_User(request):   
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.create(username=username,password=password)
        rahul_signal.send(sender=user,custom_arg='execute in creater_user view')
    return HttpResponse('Saved Successfully')