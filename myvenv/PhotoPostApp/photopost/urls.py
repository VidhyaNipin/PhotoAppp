from django.urls import path
from. import views

urlpatterns = [
    path('index/', views.indexview, name='index'),
    path('home/', views.photopostview, name='photopost'),
    path('success', views.success, name='success'),
    path('searchphoto/', views.searchauthorview, name='search'),
    path('searchcaption/', views.searchcaptionview, name='searchcaption'),
    path('photoview/', views.photoview, name='photoview'),
]
