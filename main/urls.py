from django.contrib import admin
from django.urls import path
from main.app.views import HelloAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/tes/", HelloAPIView.as_view(), name="hello"),
]
