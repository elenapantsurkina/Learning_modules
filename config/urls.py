from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lm/", include("lm.urls", namespace="lm")),
    path("lmusers/", include("users.urls", namespace="users")),
]
