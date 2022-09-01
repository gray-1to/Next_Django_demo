from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from urllib3 import HTTPResponse
from django.http import HttpResponse  
from next_django_app.functions.operate import download_test_csv_func, operate_uploaded_csv_func, operate_func

# def hello(request):
#     hw = 'Hello World!'
#     return render(request, 'base.html', {'object':hw})
from django_nextjs.render import render_nextjs_page_sync
def index(request):
    return render_nextjs_page_sync(request)

def test_top(request):
    return render_nextjs_page_sync(request)

def test_code(request):
    response = HttpResponse()
    response['mydata'] = 1
    return response

def download_test_csv(request):
    response = download_test_csv_func()
    return response

def upload_operate_test_csv(request):
    uploaded_file = request.FILES['csv_file']
    response = operate_uploaded_csv_func(uploaded_file)
    return response

def operate(request):
    uploaded_file = request.FILES['csv_file']
    plus_opt = (request.POST['plus_opt'] == "true")
    index_opt = (request.POST['index_opt'] == "true")
    response = operate_func(uploaded_file, plus_opt, index_opt)
    return response

