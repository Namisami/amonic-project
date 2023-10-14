from rest_framework import routers
from django.urls import include
from users.views import RoleViewSet, UserViewSet
from airports.views import CountryViewSet, OfficeViewSet
from users.urls import router as UsersRouter

router = routers.DefaultRouter()

router.register('users', UserViewSet) 
router.register('roles', RoleViewSet) 
router.register('countries', CountryViewSet) 
router.register('offices', OfficeViewSet) 