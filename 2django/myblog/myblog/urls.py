"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('custom_tags.urls')),
    url(r'^', include('custom_filter.urls')),
    url(r'^', include('engine_jinja2.urls')),
    url(r'^', include('custom_manager.urls')),
    url(r'^', include('merge_databases_table.urls')),
    url(r'^', include('mongodb_django.urls')),
    url(r'^', include('custom_form.urls')),
    url(r'^', include('custom_field.urls')),
    url(r'^', include('general_view.urls')),
    url(r'^', include('ajax_json.urls')),
    url(r'^', include('djangorestframework.urls')),

]