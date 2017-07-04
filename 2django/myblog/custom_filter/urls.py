from django.conf.urls import url
from custom_filter import views
urlpatterns = [
    url(r'^home2/$', views.home2)
]