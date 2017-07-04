from django import forms

from general_view.models import Task, Poem

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_id', 'name']

class AddPoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title']