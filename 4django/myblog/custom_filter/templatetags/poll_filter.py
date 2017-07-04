from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
register = template.Library()

#法一自定义
def cut_filter(value, arg):
    return value.replace(arg, '')

register.filter(name="cut_filter", filter_func=cut_filter)

#法二装饰器简化
# @register.filter()
# def cut_filter(value, arg):
#     return value.replace(arg, '')

#大写转化为小写字母
# @register.filter()
# @stringfilter
# def lower(value):
#     return value.lower()

#字符转义
# @register.filter(is_safe=True)
# def add(value, arg):
#     return mark_safe("%s %s" % (value, arg))