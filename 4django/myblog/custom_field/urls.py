from django.conf.urls import url
from custom_field import views

urlpatterns =[
    url(r'^home_field/$', views.home),
    url(r'^testlist/$', views.testlist),
    url(r'^addfile/$', views.addfile)
]