from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.app.views import (
    HelloAPIView,
    HelloViewSet,
    UserProfileViewSet,
    UserLoginApiView,
)

router = DefaultRouter()
router.register(r"tes-viewset", HelloViewSet, basename="viewset")
router.register(r"profile", UserProfileViewSet, basename="profile")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/tes-viewapi/", HelloAPIView.as_view(), name="viewapi"),
    path("api/login/", UserLoginApiView.as_view(), name="token"),
    path("api/", include(router.urls)),
]
