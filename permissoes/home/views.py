from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User 
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

# Create your views here.

@has_role_decorator('gerente')
def home(request):
     pass
 
 
def criar_usuario(request):
    user = User.objects.create_user(username="julia", password="1234")
    user.save()
    assign_role(user, 'administrativo')
    return HttpResponse('Usuario salvo')


 
 
 