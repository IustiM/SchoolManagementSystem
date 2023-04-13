from django.contrib import admin

from .models import NewUser, CustomAccountManager


class NewUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'first_name', 'last_name', 'is_active')

# class CustomAccountManagerAdmin(admin.ModelAdmin):
#     list_display = ('__all__')


admin.site.register(NewUser)
# admin.site.register(CustomAccountManager)
