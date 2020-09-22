from django.contrib import admin

# Register your models here.

from account.models import Account
from django.contrib.auth.admin import UserAdmin

from django.contrib.sites.models import Site
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','username','first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

#Add sites module to admin to create urls
admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)