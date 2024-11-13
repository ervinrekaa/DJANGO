from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
]