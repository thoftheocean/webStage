from django.shortcuts import render,HttpResponse,Http404
from ajax_json.models import  Poem
# Create your views here.

def more_poems(request):
    if request.is_ajax():
        objects = Poem.objects.all()
        print(type(objects)) #对象列表
        data = get_json_objects(objects, Poem)
        # print(data)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404()

def json_filed(field_data):
    if isinstance(field_data, str):
        return "\"" + field_data + "\""
    if isinstance(field_data, bool):
        if field_data == 'False':
            return 'false'
        else:
            return 'true'
    return str(field_data)


def json_encode_dict(dict_data):
    json_data = "{"
    for (k, v) in dict_data.items():
        json_data = json_data +json_filed(k) + ": " + json_filed(v) + ", "
    json_data = json_data[:-2] + "}"
    print('字典编码', json_data)
    return json_data

def json_encode_list(list_data):
    json_res = "["
    for item in list_data:
        json_res = json_res + json_encode_dict(item) + ", "
    print('列表编码', json_res[:-2] + "]")
    return json_res[:-2] + "]"


def get_json_objects(objects, model_meta):
    concrete_model = Poem._meta.concrete_model
    list_data = []
    print(objects)
    for obj in objects:
        dict_data = {}
        for field in concrete_model._meta.local_fields:
            if field.name == 'id':
                continue
            value = field.value_from_object(obj)
            dict_data[field.name] = value

        list_data.append(dict_data)
    print(type(list_data), '初始json数据', list_data) #列表里面存放的是字典

    data = json_encode_list(list_data)
    # data = str(list_data)
    print(type(data), '编码后的json数据', data)
    return data


import ast

def add(request):
    if request.is_ajax() and request.POST:
        print('开始添加')
        json_str = request.POST.get('poems')
        print(type(json_str))  #获取的数据时str
        data = "post success"
        #输入的数据：[{'title': '相思', 'poem_id': 1, 'author': '王维'}] 转化为列表
        json_list = ast.literal_eval(json_str)

        print(type(json_list))
        for item in json_list:
            new_obj = Poem()
            for filed in item:
                setattr(new_obj, filed, item[filed])
            print(new_obj.author, new_obj.title, new_obj.poem_id)
            new_obj.save()
        return HttpResponse(data, content_type='application/text')
    else:
        return Http404
