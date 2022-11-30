from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User 
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.permissions import revoke_permission, grant_permission 
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

# Create your views here.

@has_role_decorator('administrativo')
def home_admin(request):
    
     return HttpResponse('Pagina administrativo')
 
def home_comercial(request):
    
    return HttpResponse('Pagina Comercial')
 
 
def criar_usuario(request):
    user = User.objects.create_user(username="julia", password="1234")
    user.save()
    assign_role(user, 'comercial')
    return HttpResponse('Usuario salvo')


 
 
 