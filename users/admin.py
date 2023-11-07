from django.contrib import admin

from .models import User, Role, Office, Country

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Role)
admin.site.register(Office)
