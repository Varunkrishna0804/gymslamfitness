from django.urls import path
from Slamapp import views

urlpatterns = [
   path('',views.Home,name="Home")
]