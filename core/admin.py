from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields': ('first_name','last_name','counterparty')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
    )
    add_fieldsets = ((None, {'fields': ('email','password1','password2')}),)
    list_display = ('id','email','counterparty_display','first_name','last_name','is_staff')
    search_fields = ('email','first_name','last_name','counterparty__display_name')
    ordering = ('id',)

    @admin.display(description="Контрагент")
    def counterparty_display(self, obj):
        return obj.counterparty.display_name if getattr(obj, 'counterparty', None) else None
