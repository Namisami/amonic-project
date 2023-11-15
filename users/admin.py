from django.contrib import admin

from .models import User, Role, Office, Country, Error, Visit

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Role)
admin.site.register(Office)
admin.site.register(Error)
admin.site.register(Visit)
