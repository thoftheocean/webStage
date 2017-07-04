from django.shortcuts import render,HttpResponseRedirect
from general_view.models import Task
from django.views.generic import TemplateView, ListView, View
from general_view.forms import AddTaskForm

def index(request):
    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

#显示所有的task
class ShowTasksView(ListView):
    template_name = 'tasks.html'
    model = Task

#显示一个task
class DisplaySingleTaskView(TemplateView):
    template_name = 'single_task.html'

    def get_context_data(self, **kwargs):
        context = super(DisplaySingleTaskView, self).get_context_data(**kwargs)
        task_id = self.kwargs.get('task_id', 0)
        context['task'] = Task.objects.get(task_id=task_id)
        return context

#表单通用视图,作为添加task和poem的视图函数
class AddModelView(View):
    form_class = AddTaskForm
    template_name = 'add_task.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/success')
