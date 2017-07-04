from django.shortcuts import render
from custom_manager.models import ToDo
# Create your views here.
def todolist(request):
    # return render(request,'todolist.html', {'showType': '所有列表', 'todolist': ToDo.objects.all()})

    #自定义manager
    # return render(request, 'todolist.html', {'showType': '未完成的事件', 'todolist': ToDo.todolist.all().filter(is_done=False)})

    #自定义未完成事件查询
    # return render(request, 'todolist.html', {'showType': '未完成的事件', 'todolist': ToDo.incomplete.all()})

    #自定义高优先级查询
    # return render(request, 'todolist.html', {'showType': '高优先级事件', 'todolist': ToDo.high.all()})

    # 自定义未完成事件查询和高优先级查询
    # return render(request, 'todolist.html', {'showType': '未完成事件', 'todolist': ToDo.objects.incomplete()})
    # return render(request, 'todolist.html', {'showType': '高优先级事件', 'todolist': ToDo.objects.high()})

    #方法三
    # return render(request, 'todolist.html', {'showType': '高优先级未完成的事件', 'todolist': ToDo.objects.all().high().incomplete()})

    #方法四
    return render(request, 'todolist.html', {'showType': '高优先级未完成事件', 'todolist': ToDo.objects.high().incomplete()})
