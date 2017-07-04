from django.db import models
import ast

#自定义ListFild
class ListFiled(models.TextField):
    description = 'just a listfild'

    def __init__(self, *args, **kwargs):
        super(ListFiled, self).__init__(*args, **kwargs)

    def from_db_value(self,value,expression,coon, context):
        print('from_db_values')

        if not value:
            value = []
        if isinstance(value, list):
            return value
        print('value type', type(value))
        return ast.literal_eval(value)

    #数据保存时，就是调用这个方法。以列表信息存入数据库
    def get_prep_value(self, value):
        print('get_pre_value')

        if not value:
            return value
        print('value type', type(value))
        return str(value)

from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContextTypeRestrictedFileField(FileField):
    def __init__(self, content_type=None, max_upload_size=None, **kwargs):
        self.content_type = content_type
        self.max_upload_size = max_upload_size
        super(ContextTypeRestrictedFileField, self).__init__(**kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContextTypeRestrictedFileField, self).clean(*args, **kwargs)
        file = data.file
        try:
            type = file.content_type
            if type != self.content_type:
                print('上传文件类型出错')
                raise forms.ValidationError('pls upload right filetype')

            if file.size > self.max_upload_size:
                print('超出最大文件要求')
                raise forms.ValidationError('exceed max uploadsize')
        except AttributeError:
            print("error")
            pass
        return data