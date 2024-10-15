from django.contrib import admin
from .models import Gallery, Vendor, Menu

# Register your models here.
class MenuInline(admin.StackedInline):
    model = Menu
    extra = 0
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone', 'website', 'logo')

    inlines = [MenuInline]

admin.site.register(Gallery)