from django.conf.urls import url, include
from django.urls import path
from landing import views

urlpatterns = [
    url(r'^landing123/', views.landing, name='landing')
]
