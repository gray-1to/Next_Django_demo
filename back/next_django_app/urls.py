from django.urls import path
# from .views import hello
from .views import index, test_code, operate, upload_operate

urlpatterns = [
    # path('', hello, name='hello'),
    path("", index, name="index"),
    path("api/test_code", test_code, name="test_code"),
    path("api/operate", operate, name="operate"),
    path("api/upload_operate", upload_operate, name="upload_operate")
]