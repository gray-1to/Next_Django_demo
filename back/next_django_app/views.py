from django.shortcuts import render

# def hello(request):
#     hw = 'Hello World!'
#     return render(request, 'base.html', {'object':hw})
from django_nextjs.render import render_nextjs_page_sync
def index(request):
    return render_nextjs_page_sync(request)