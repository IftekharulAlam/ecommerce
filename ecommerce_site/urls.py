from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.toIndex, name='index'),
    path('index.html', views.toIndex, name='index'),
    path('about.html',views.toAbout, name='about'),
    path('contact.html',views.toContact, name='contact'),
    path('shop.html', views.toShop, name='shop'),
    path('shop-single.html',views.toShopSingle, name='shopsingle'),
    path('login', views.toLogin, name="login"),
    path('register', views.toRegister, name="register")


]
