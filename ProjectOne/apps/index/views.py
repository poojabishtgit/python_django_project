from django.shortcuts import render
from django.http import HttpResponse
from  .models import Register

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
   name = register.POST['name']
   email = register.POST['email']
   phone = register.POST['phone']
   address = register.POST['address']
   username = register.POST['username']
   password = register.POST['password']
   cpassword = register.POST['cpassword']
