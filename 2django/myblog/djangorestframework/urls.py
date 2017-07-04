from django.conf.urls import url
from djangorestframework import views

urlpatterns =[
    url(r'^rest_poems/$', views.PoemListView.as_view(), name='poem_list'),
    url(r'^rest_poems/(?P<pk>[0-9]+)$', views.poem_detail, name='poem_detail')
]