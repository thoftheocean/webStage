from django import forms
from demo.models import Publisher
from django.core.exceptions import ValidationError

# class PublisherForm(forms.Form):
#     name = forms.CharField(label='名称',error_messages={"required":'这项必须填写'})
#     address = forms.CharField(label='地址',error_messages={"required":'这项必须填写'})
#     city = forms.CharField(label='城市',error_messages={"required":'这项必须填写'})
#     state_province = forms.CharField(label='省份',error_messages={"required":'这项必须填写'})
#     country = forms.CharField(label='国家',error_messages={"required":'这项必须填写'})
#     website = forms.URLField(label='网址',error_messages={"required":'这项必须填写'})


#
# #表单字段验证器
# def validate_name(value):
#     print(value)
#     try:
#         Publisher.objects.get(name=value)
#         raise ValidationError('%s的信息已经存在' % value)
#     except Publisher.DoesNotExist:
#         pass
#
#
# class PublisherForm(forms.ModelForm):
#     name = forms.CharField(label='名称', validators=[validate_name])
#     class Meta:
#         model = Publisher
#         exclude = ('id', )




#clean_filedname,验证字段，针对某个字段进行验证。

# class PublisherForm(forms.ModelForm):
#     def clean_name(self):
#         value=self.cleaned_data.get('name')
#         try:
#             Publisher.objects.get(name=value)
#             raise ValidationError('%s的信息已经存在' % value)
#         except Publisher.DoesNotExist:
#             pass
#         return value
#
#     class Meta:
#         model = Publisher
#         exclude = ('id', )


#3、表单clean方法，可针对整个表单进行验证。
class PublisherForm(forms.ModelForm):
    def clean(self):
        cleaned_data=super(PublisherForm,self).clean()

        value=cleaned_data.get('name')
        try:
            Publisher.objects.get(name=value)
            self._errors['name']=self.error_class(['%s的信息已经存在' % value])
        except Publisher.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Publisher
        exclude = ('id', )