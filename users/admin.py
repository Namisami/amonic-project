from django.contrib import admin

from .models import User, Role, Office, Country, Error

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Role)
admin.site.register(Office)
admin.site.register(Error)
