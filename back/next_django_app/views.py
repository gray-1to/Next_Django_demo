from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from urllib3 import HTTPResponse
from django.http import HttpResponse  
from extensions.operate import operate_file

# def hello(request):
#     hw = 'Hello World!'
#     return render(request, 'base.html', {'object':hw})
from django_nextjs.render import render_nextjs_page_sync
def index(request):
    # request.session['test_code'] = 'Djangoで入れられた変数です'
    return render_nextjs_page_sync(request)

def test_code(request):
    response = HttpResponse()
    response['mydata'] = 1
    return response

def operate(request):
    response = operate_file()
    return response
