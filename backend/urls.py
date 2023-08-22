from django.urls import path
from . import views

#urlConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('get-roles/', views.get_roles)
]


