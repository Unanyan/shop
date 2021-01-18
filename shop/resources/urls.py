from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('how_to_order/', views.how_to_order, name='how_to_order'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
