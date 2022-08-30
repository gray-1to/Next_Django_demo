from django.urls import path
# from .views import hello
from .views import index, test_code, operate

urlpatterns = [
    # path('', hello, name='hello'),
    path("", index, name="index"),
    path("api/test_code", test_code, name="test_code"),
    path("api/operate", operate, name="operate")
]