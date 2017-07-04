# -*- coding: utf-8 -*-
from mongoengine import *

# Create your models here.
class Poem(Document):
    #默认类名为表明，meta指定表的名字
    meta = {
        'collection': 'poem_data'
    }
    poem_id = SequenceField(required=True, primary_key=True)
    author = StringField()
    title = StringField()

    @queryset_manager
    def show_newest(doc_cls, queryset):
        return queryset.order_by('-poem_id')
