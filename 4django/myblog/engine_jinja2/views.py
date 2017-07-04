from django.shortcuts import render

# Create your views here.
def home3(request):
    return render(request, 'home.html', {"tmpValue": [1, 2, 3]})