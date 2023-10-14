from rest_framework import routers
from users.views import RoleViewSet, UserViewSet
from airports.views import CountryViewSet, OfficeViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet) 
router.register('roles', RoleViewSet) 
router.register('countries', CountryViewSet) 
router.register('offices', OfficeViewSet) 
