from django.urls import path
# from .views import hello
from .views import index, test_top, test_code, download_test_csv, upload_operate_test_csv, operate

urlpatterns = [
    # path('', hello, name='hello'),
    path("", index, name="index"),
    path("test_top", test_top, name="test_top"),
    path("api/test_code", test_code, name="test_code"),
    path("api/download_test_csv", download_test_csv, name="download_test_csv"),
    path("api/upload_operate_test_csv", upload_operate_test_csv, name="upload_operate_test_csv"),
    path("api/operate", operate, name="operate")
]