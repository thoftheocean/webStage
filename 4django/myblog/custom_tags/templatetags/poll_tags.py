from django import template
from datetime import datetime
from custom_tags.models import Poem
register = template.Library()

#自定义法一
class AllenDateNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        return datetime.now().strftime(self.format_string)

def dateAllen(parse,token):
    try:
        tagname, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("invalid agrs")
    return AllenDateNode(format_string[1:-1])

register.tag(name='dateAllen', compile_function=dateAllen)

#法二django自带装饰器，简化注册

# class AllenDateNode(template.Node):
#     def __init__(self, format_string,):
#         self.format_string = format_string
#
#     def render(self, context):
#         now = datetime.now().strftime(self.format_string)
#         context['mytime'] = now
#         return ''
#
#
# @register.tag()
# def dateAllen(parse,token):
#     try:
#         tagname, format_string = token.split_contents()
#     except ValueError:
#         raise template.TemplateSyntaxError("invalid agrs")
#     return AllenDateNode(format_string[1:-1])

# 法三
# class AllenDateNode(template.Node):
#     def __init__(self, format_string, asvar):
#         self.format_string = format_string
#         self.asvar = asvar
#
#     def render(self, context):
#         now = datetime.now().strftime(self.format_string)
#         if self.asvar:
#             context[self.asvar] = now
#             return ""
#         else:
#             return now
# @register.tag()
# def dateAllen(parse,token):
#     args = token.split_contents()
#     asvar = None
#     if len(args) == 4 and args[-2] == 'as':
#         asvar = args[-1]
#     elif len(args)!=2:
#         raise template.TemplateSyntaxError("invalid agrs")
#     return AllenDateNode(args[1][1:-1], asvar)


#法四  自带装饰器自定义名字
# class AllenDateNode(template.Node):
#     def __init__(self, format_string, asvar):
#         self.format_string = format_string
#         self.asvar = asvar
#
#     def render(self, context):
#         now = datetime.now().strftime(self.format_string)
#         if self.asvar:
#             context[self.asvar] = now
#             return ""
#         else:
#             return now
#
# @register.assignment_tag()
# def get_current_time(format_string):
#     return datetime.now().strftime(format_string)

#自定义标签实现诗词呈现，渲染到模板
# @register.inclusion_tag("resultes.html")
# def poems_of_author(author_name):
#     poems = Poem.objects.filter(author=author_name)
#     return {"poems": poems, "author_name": author_name}
