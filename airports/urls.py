from rest_framework import routers

from .views import OfficeViewSet, CountryViewSet, AirportViewSet, AircraftViewSet, RouteViewSet, ScheduleViewSet

router = routers.DefaultRouter()
router.register(r'offices/', OfficeViewSet, 'Office')
router.register(r'countries/', CountryViewSet, 'Country')
router.register(r'airports/', AirportViewSet, 'Airport')
router.register(r'aircrafts/', AircraftViewSet, 'Aircraft')
router.register(r'routes/', RouteViewSet, 'Route')
router.register(r'schedules/', ScheduleViewSet, 'Schedule')
