#coding:utf-8
from django.shortcuts import render,render_to_response,redirect

from django.contrib.auth.models import User
from django.template import loader,RequestContext,Template

from django.http import HttpRequest,HttpResponse

from demo.models import Publisher

# Create your views here.
def demo(request):

    # print request.get_full_path()

    user_list = User.objects.all()

    #查看usr_list生成的sql语句
    # print user_list.query

    athlete = '0'
    valuel='hello world'
    valuel2=1
    import datetime
    valuel3=datetime.datetime.now()
    valuel4='<h1>hello</h1>'
    valuel5=Template("<a href='http://www.baidu.com'>百度</a>")
    # return render(request,'table.html',{'user_list':user_list,'athlete':'0'})
    # return render_to_response('table.html', {'user_list': user_list})

    #locals()获取所有的变量
    # print locals()
    # return render_to_response('table.html',locals(),context_instance=RequestContext)


    return render(request,'table.html',locals())
    #页面跳转
    # return redirect('http://www.baidu.com')



def test(request):
    return render(request,'a.html')


def add_publisher(request):

#不使用Form情况
    # if request.method == 'POST':
    #     print(request.method)
    #     print(request.POST)
    #     name = request.POST['name']
    #     address = request.POST['address']
    #     city = request.POST['city']
    #     state_province = request.POST['state_province']
    #     country = request.POST['country']
    #     website = request.POST['website']
    #     Publisher.objects.create(
    #         name=name,
    #         address=address,
    #         city=city,
    #         state_province=state_province,
    #         country=country,
    #         website=website,
    #     )
    #     return HttpResponse('添加出版社成功')
    #
    # else:
    #     return render(request,'add_publisher.html',locals())

#使用django From情况
    # from demo.models import Publisher
    # from demo.forms import PublisherForm
    # if request.method == 'POST':
    #     publisher_form=PublisherForm(request.POST)
    #     if publisher_form.is_valid():
    #         Publisher.objects.create(
    #             name=publisher_form.cleaned_data['name'],
    #             address=publisher_form.cleaned_data['address'],
    #             city=publisher_form.cleaned_data['city'],
    #             state_province=publisher_form.cleaned_data['state_province'],
    #             country=publisher_form.cleaned_data['country'],
    #             website=publisher_form.cleaned_data['website'],
    #             )
    #         return HttpResponse('添加出版社成功')
    # else:
    #     publisher_form=PublisherForm()
    # return render(request,'add_publisher.html',locals())

#使用django ModelForm的情况
    from demo.models import Publisher
    from demo.forms import PublisherForm
    if request.method == 'POST':
        publisher_form=PublisherForm(request.POST)
        if publisher_form.is_valid():
            publisher_form.save()
            return HttpResponse('添加出版社成功')
    else:
        publisher_form=PublisherForm()
    return render(request,'add_publisher.html',locals())