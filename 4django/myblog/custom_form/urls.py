from django.conf.urls import url
from custom_form import views

urlpatterns = [
    url(r'^home_form/$', views.home, name='home'),
    url(r'^add_poem/$', views.add, name='add'),
]