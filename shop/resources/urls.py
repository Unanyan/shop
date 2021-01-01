from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('privacy_and_policy/', views.privacy_and_policy, name='privacy'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms'),
]
