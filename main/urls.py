from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.app.views import HelloAPIView, HelloViewSet

router = DefaultRouter()
router.register(r"tes-viewset", HelloViewSet, basename="viewset")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/tes-viewapi/", HelloAPIView.as_view(), name="viewapi"),
    path("api/", include(router.urls)),
]
