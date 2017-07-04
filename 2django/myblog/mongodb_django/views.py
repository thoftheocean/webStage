# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from mongodb_django.models import Poem

# Create your views here.
def home(request):
    return render(request, 'home_mongodb.html', {"show_title": "所有诗词信息", "poems": Poem.objects.all()})

def add(request):
    if request.method == 'POST':
        author = request.POST.get('author', "")

        poem = Poem(author=author)
        poem.save()
        title = request.POST.get("title", "")
        poem.title = title
        poem.tag = 'tag'
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add.html')

def search(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        poems = Poem.show_newest(author=author)

        return render(request, 'home.html', {"show_title": "查询结果", "poems": poems})

    else:
        return render(request, 'search.html')

def modify(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        author = request.POST.get('author', "")
        title = request.POST.get("title", "")
        poems = Poem.objects(poem_id=id)
        for poem in poems:
            poem.update(author=author, title=title)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'modify.html')

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        poems = Poem.objects(poem_id=id)
        for poem in poems:
            poem.delete()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'delete.html')