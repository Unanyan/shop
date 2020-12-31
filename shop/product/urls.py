from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('child/', views.child, name='child'),
]
