from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Role, Office, Country, Error, Visit
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'is_staff')
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'office')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser')}),
        ('Time manage', {'fields': ('last_login', 'last_logout')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    exclude = ('username',)
    # search_fields = ('email',)
    ordering = ('email',)
    # filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Country)
admin.site.register(Role)
admin.site.register(Office)
admin.site.register(Error)
admin.site.register(Visit)
