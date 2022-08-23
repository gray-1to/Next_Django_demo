from django.urls import path
# from .views import hello
from .views import index

urlpatterns = [
    # path('', hello, name='hello'),
    path("", index, name="index"),
]