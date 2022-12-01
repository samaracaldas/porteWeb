from django.urls import path
from . import views 


urlpatterns = [
    path('usuario/', views.criar_usuario),
    path('admin/', views.home_admin),   
    path('administrativo/', views.home_admin),   
    path('comercial/', views.home_comercial),
]
