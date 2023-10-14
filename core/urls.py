from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
