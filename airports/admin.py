from django.contrib import admin

from .models import Country, Office, Aircraft, Airport, Route, Schedule

admin.site.register(Country)
admin.site.register(Office)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Route)
admin.site.register(Schedule)
