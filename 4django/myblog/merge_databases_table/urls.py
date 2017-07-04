from django.conf.urls import url
from merge_databases_table import views
urlpatterns = [
    url(r'^todolist1/$', views.todolist1)
]