from django.contrib import admin
from account.models import User
# Register your models here.
# admin.site.register(User)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.forms import UserAdminCreationForm, UserAdminChangeForm



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email','password']
    list_filter = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        
        ('Permissions', {'fields': ('is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', )}
        ),
        (None, {
            'classes': ('wide',),
            'fields': ('password', )}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()



admin.site.register(User, UserAdmin)