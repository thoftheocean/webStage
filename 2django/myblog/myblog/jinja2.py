from jinja2 import Environment
from custom_filter.templatetags.poll_filter import lower

def environment(**options):
    env = Environment(**options)
    env.filters['allen_lower'] = lower  #引入自定义的过滤器,allen_lower为过滤器名
    return env
