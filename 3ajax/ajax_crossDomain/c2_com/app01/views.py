#  coding:utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def test(request):
    # response = HttpResponse('...')
    # return response
    # s1
    # response = HttpResponse('...')
    # response['Access-Control-Allow-Origin'] = "*"
    # return response

    # s2
    # response = HttpResponse('...')
    # response['Access-Control-Allow-Origin'] = "*"
    #
    # if request.method == "OPTIONS":
    #     #预检操作
    #     response['Access-Control-Allow-Headers'] = "k1,k2"  # 允许Header发送k1,k2
    #     response['Access-Control-Allow-Methods'] = "PUT,DELETE"  # 允许发送put和delete请求
    #     response['Access-Control-Max-Age'] = 10 # 预检保存10秒
    # return response

    # s3
    # response = HttpResponse('...')
    # response['Access-Control-Allow-Origin'] = "*"
    #
    # if request.method == "OPTIONS":
    #     response['Access-Control-Allow-Headers'] = "k1,k2"
    #     response['Access-Control-Allow-Methods'] = "PUT,DELETE"
    #     response['Access-Control-Max-Age'] = 10
    #
    # response['custom-header'] = 'seven'
    # response['Access-Control-Expose-Headers'] = 'custom-header'
    #
    # return response

    # s4
    print(request.COOKIES)
    response = HttpResponse('...')
    response['Access-Control-Allow-Origin'] = "http://localhost:63342"
    response['Access-Control-Allow-Credentials'] = "true"

    # if request.method == "OPTIONS":
    #     response['Access-Control-Allow-Headers'] = "k1,k2"
    #     response['Access-Control-Allow-Methods'] = "PUT,DELETE"
    #     response['Access-Control-Max-Age'] = 10
    #
    # response.set_cookie('my_cookie', 'seven')
    # return response

    # s5
    # func_name = request.GET.get('callback')
    # data = '{"k1":123, "k2":456}'
    # temp = "%s(%s)" % (func_name, data)
    # #  call({"k1":123, "k2":456})
    # response = HttpResponse(temp)
    # return response

@csrf_exempt
def cors(request):
    n1 = request.POST.get('n1')
    n2 = request.POST.get('n2')
    result = int(n1) + int(n2)
    response = HttpResponse(result)
    response['Access-Control-Allow-Origin'] = "*"
    return response


@csrf_exempt
def jsonp(request):
    print(request.GET)
    print(request.POST)

    func_name = request.GET.get('callback')
    n1 = request.GET.get('n1')
    n2 = request.GET.get('n2')

    result = int(n1) + int(n2)

    temp = "%s(%s)" % (func_name, result)
    response = HttpResponse(temp)
    return response