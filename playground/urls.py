from django.urls import URLPattern, path,include
from . import views

urlpatterns = [
    path('',views.sai),
    path('templates/traing/register.html',views.reg)
]  