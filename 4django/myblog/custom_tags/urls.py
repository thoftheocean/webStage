from django.conf.urls import url
from custom_tags import views
urlpatterns = [
    url(r'^home1/$', views.home1)
]