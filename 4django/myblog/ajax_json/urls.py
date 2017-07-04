from django.conf.urls import url
from ajax_json import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'ajax_json/$', TemplateView.as_view(template_name='ajax_json.html')),
    url(r'ajax/more/$', view=views.more_poems),
    url(r'ajax/add/$', view=views.add),
]