from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'auth', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
