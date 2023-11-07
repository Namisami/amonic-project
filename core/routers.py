from rest_framework import routers
from users.views import RoleViewSet, UserViewSet, OfficeViewSet, CountryViewSet
from airports.views import AirportViewSet, AircraftViewSet, RouteViewSet, ScheduleViewSet, CabinTypeViewSet, TicketViewSet, SurveyViewSet, AmentityViewSet, AmentityTicketViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet) 
router.register('roles', RoleViewSet) 
router.register('countries', CountryViewSet) 
router.register('offices', OfficeViewSet) 
router.register('airports', AirportViewSet)
router.register('aircrafts', AircraftViewSet)
router.register('routes', RouteViewSet)
router.register('schedules', ScheduleViewSet)
router.register('cabin_types', CabinTypeViewSet)
router.register('tickets', TicketViewSet)
router.register('surveys', SurveyViewSet)
router.register('amentities', AmentityViewSet)
router.register('amentity-tickets', AmentityTicketViewSet)
