from django.conf.urls import url
from custom_manager import views
urlpatterns = [
    url(r'^todolist/$', views.todolist)
]