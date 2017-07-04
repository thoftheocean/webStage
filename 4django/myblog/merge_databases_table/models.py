from django.db import models

# Create your models here.

#方法一
class IncompleteTodoManager(models.Manager):
    def get_queryset(self):
        return super(IncompleteTodoManager, self).get_queryset().filter(is_done=False)

class HighPriorityManager(models.Manager):
    def get_queryset(self):
        return super(HighPriorityManager, self).get_queryset().filter(priority=1)

#方法二
class ToDoManager(models.Manager):
    def incomplete(self):
        return self.filter(is_done=False)

    def high(self):
        return self.filter(priority=1)

#方法三
# class TodoQuerySet(models.QuerySet):
#     def incomplete(self):
#         return self.filter(is_done=False)
#
#     def high(self):
#         return self.filter(priority=1)
#
# class NewTodoManager(models.Manager):
#     def get_queryset(self):
#         return TodoQuerySet(self.model, using=self._db)
#方法四
class TodoQuerySet(models.QuerySet):
    def incomplete(self):
        return self.filter(is_done=False)

    def high(self):
        return self.filter(priority=1)

class NewTodoManager(models.Manager):
    def get_queryset(self):
        return TodoQuerySet(self.model, using=self._db)

    def incomplete(self):
        return self.get_queryset().incomplete()

    def high(self):
        return self.get_queryset().high()

#方法三和方法四区别。法四在newTodoManager中调用了两个方法，就省去了all()的使用。


class ToDo(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return '%s-%d' %(self.content, self.priority)



    #自定义manager
    todolist = models.Manager()

    #自定义未完成事件查询
    incomplete = IncompleteTodoManager()

    #自定义高优先级查询
    high = HighPriorityManager()

    #自定义未完成事件查询和高优先级查询
    # objects = ToDoManager()

    #方法三和四
    objects = NewTodoManager()


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'user'
