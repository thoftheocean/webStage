from django.conf.urls import url
from mongodb_django import views
urlpatterns = [
    url(r'^home_mongodb/$', views.home, name='home'),
    url(r'^add/', views.add, name='add'),
    url(r'^search/', views.search, name='search'),
    url(r'^modify/', views.modify, name='modify'),
    url(r'^delete/', views.delete, name='delete'),
]