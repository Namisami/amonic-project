from rest_framework import routers
from users.views import RoleViewSet, UserViewSet
from airports.views import CountryViewSet, OfficeViewSet, AirportViewSet, AircraftViewSet, RouteViewSet, ScheduleViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet) 
router.register('roles', RoleViewSet) 
router.register('countries', CountryViewSet) 
router.register('offices', OfficeViewSet) 
router.register('airports', AirportViewSet)
router.register('aircrafts', AircraftViewSet)
router.register('routes', RouteViewSet)
router.register('schedules', ScheduleViewSet)
