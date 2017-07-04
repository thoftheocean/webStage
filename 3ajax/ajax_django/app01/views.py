import json
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):

    return render(request, 'index.html')

def error_xhr(request):

    return render(request, 'errors_xhr.html')


def error_jq(request):

    return render(request, 'error_jq.html')


@csrf_exempt
def test(request):
    ret = {'status': True, 'data': None}

    try:
        n1 = request.POST.get('n1')
        n2 = request.POST.get('n2')
        content = int(n1) + int(n2)
        ret['data'] = content
    except Exception as ex:
        ret['status'] = False
        ret['error'] = str(ex)

    response = HttpResponse(json.dumps(ret))
    response.status_code = 200
    return response