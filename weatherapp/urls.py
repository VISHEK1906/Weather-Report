from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.index, name="index"),
    # path("index3",views.index3, name="index3"),
    # path("index4",views.index4, name="index4"),
    path("base",views.base, name="base"),
    path("news",views.news, name="news"),
    path("livecameras",views.livecameras, name="livecameras"),
    path("photos",views.photos, name="photos"),
    path("contact",views.contact, name="contact"),
    path("subscribe",views.subscribe, name="subscribe"),
    # path("login",views.login, name="login"),
    # path("register",views.register, name="register"),
    # path("logout",views.logout, name="logout"),
]