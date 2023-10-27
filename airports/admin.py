from django.contrib import admin

from .models import Country, Office, Aircraft, Airport, Route, Schedule, CabinType, Ticket, Survey

admin.site.register(Country)
admin.site.register(Office)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(CabinType)
admin.site.register(Ticket)
admin.site.register(Survey)
