from django.urls import path
from .import views

urlpatterns = [
    path('',views.registration  , name='registration'),
    path('form',views.form , name = 'form'),
    path('index' ,views.login_request, name = 'index')
]