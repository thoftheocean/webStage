from django.conf.urls import url
from general_view.views import IndexView,ShowTasksView, DisplaySingleTaskView,AddModelView
# from .views import index, IndexView, ShowTasksView, DisplaySingleTaskView,AddModelView
from django.views.generic import TemplateView, RedirectView
from general_view.forms import AddPoemForm

urlpatterns = [
    #模板视图
    # url(r'^index/$', TemplateView.as_view(template_name='index.html')),
    #自己在view中重新定义Templateview
    url(r'^index/$', IndexView.as_view()),
    #显示所有的task
    url(r'^tasks/$', ShowTasksView.as_view()),
    #根据task的id获取任务
    url(r'^task/(?P<task_id>\d+)/$', DisplaySingleTaskView.as_view()),
    #重定向视图
    url(r'^redirect_baidu/$', RedirectView.as_view(url='http://baidu.com')),
    #增加添加task的表单视图
    url(r'^addtask/$', AddModelView.as_view()),
    url(r'^success/$', TemplateView.as_view(template_name='post_success.html')),
    # 增加添加poem的表单视图
    url(r'^addpoem/$', AddModelView.as_view(form_class=AddPoemForm)),
]



# urlpatterns = [
#     url(r'^index/$', IndexView.as_view()),
#     url(r'^redirect/$', RedirectView.as_view(url='http://baidu.com')),
#     url(r'^tasks/$', ShowTasksView.as_view()),
#     url(r'^task/(?P<task_id>\d+)/$', DisplaySingleTaskView.as_view()),
#     url(r'^addtask/$', AddModelView.as_view()),
#     url(r'^addpoem/$', AddModelView.as_view(form_class = AddPoemForm)),
#
#     url(r'^success/$', TemplateView.as_view(template_name='post_success.html')),
# ]