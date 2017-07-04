from django import forms
from .models import Poem
from django.core.validators import ValidationError

# class AddForm(forms.Form):
#     author = forms.CharField(label='作者')
#     title = forms.CharField(label='标题')
#

class AddForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title']

    #自定义表单验证，allen必须在author中
    # def clean_author(self):
    #     print('author必须包含allen')
    #     data = self.cleaned_data['author']
    #     if 'allen' not in data:
    #         raise ValidationError('not has allen')
    #     return data

    #验证数据是否存在
    def clean(self):
        print('验证数据是否存在')
        author = self.cleaned_data['author']
        title = self.cleaned_data['title']
        object = Poem.objects.filter(author=author, title=title)
        if object:
            raise ValidationError('dup')
