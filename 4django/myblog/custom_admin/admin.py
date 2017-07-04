from django.contrib import admin
from django import forms
from custom_admin.models import Poem, Article
from django.shortcuts import render
from custom_admin.forms import SetTypeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#--------------自定义useradmin--和modeladmin-------

# class MyUserAdmin(UserAdmin):
#     #自定义字段
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     #自定义过滤
#     list_filter = ('is_staff',)
#     #自定义搜索字段
#     search_fields = ('last_name',)
#
# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)
#
#
# class PoemModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'timestamp', 'author']
#     #设置作者链接
#     list_display_links = ['author']
#     #调用搜索框
#     search_fields = ['title']
#     #设置可编辑框
#     list_editable = ['title']
#     list_filter = ['author']
#
#     # change_form_template = 'change_form.html'
#     #
#     # class Meta:
#     #     model = Poem
# admin.site.register(Poem, PoemModelAdmin)

#------------自定义admin widget和基本操作------------

# 设置input框的样式
# class SubInputText(forms.TextInput):
#     class Media:
#         css = {
#             'all' : ('input.css',)
#         }
#
# class PoemForm(forms.ModelForm):
#     class Meta:
#         model = Poem
#         fields = ['author','title','type']
#         widgets = {
#             'author' : forms.Textarea(attrs={'cols':'20','rows':'1'}),
#             'title' : SubInputText(),
#             'type': forms.RadioSelect,
#         }
#
#
# class PoemModelAdmin(admin.ModelAdmin):
#     form = PoemForm
#
#     # 打印poem title操作
#     def print_poem(self, request, queryset):
#         pass
#         for qs in queryset:
#             print(qs)
#
#     # 更改诗词的类型
#     def set_type_action(self, request, queryset):
#         for qs in queryset:
#             qs.type = 2
#             qs.save()
#
#         #定义执行后的提示消息
#         self.message_user(request, '%d poems  will be changed  with type:2'% len(queryset))
#
#     # 更改set_type_action的名字为change_type
#     set_type_action.short_description = 'change_type'
#
#     actions = [print_poem, set_type_action]
#
# admin.site.register(Poem, PoemModelAdmin)
# admin.site.register(Article)

#-------------设置复杂的操作-----------
class SubInputText(forms.TextInput):
    class Media:
        css = {
            'all' : ('input.css',)
        }

class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author','title','type']
        widgets = {
            'author' : forms.Textarea(attrs={'cols':'20','rows':'1'}),
            'title' : SubInputText(),
            'type': forms.RadioSelect,
        }


class PoemModelAdmin(admin.ModelAdmin):
    form = PoemForm

    # 打印poem title操作
    def print_poem(self, request, queryset):
        pass
        for qs in queryset:
            print(qs)

    # 更改诗词的类型
    def set_type_action(self, request, queryset):
        if request.POST.get('post'):
            form = SetTypeForm(request.POST)
            if form.is_valid():
                type = form.cleaned_data['type']
            for qs in queryset:
                qs.type = type
                qs.save()
            # 定义执行后的提示消息
            self.message_user(request, "%d poems were changed with type:%d" % (len(queryset), type))
            return None
        else:
            return render(request, 'set_type.html'
                          , {'form': SetTypeForm(
                                     initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
                          , 'objects': queryset})

    #在poem中取消say_hello这个全局操作
    def get_actions(self, request):
        actions = super(PoemModelAdmin, self).get_actions(request)
        if 'say_hello' in actions:
            del actions['say_hello']
        return actions

    # 更改set_type_action的名字为change_type
    set_type_action.short_description = 'change_type'

    actions = [print_poem, set_type_action]
    #禁用所有的actions
    # actions=None

#全局添加操作say_hello
def say_hello(modeladmin, req, queryset):
    print('hello')

admin.site.register(Poem, PoemModelAdmin)
admin.site.register(Article)
admin.site.add_action(say_hello)
admin.site.disable_action('delete_selected')