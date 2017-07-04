from django.conf.urls import include, url
from django.contrib import admin
from app01 import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'c2_com.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', views.test),
    url(r'^cors/', views.cors),
    url(r'^jsonp/', views.jsonp),
]
