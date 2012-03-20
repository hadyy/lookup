from django.contrib import admin
from kuwaittl.lookup.models import *
from django.utils.translation import ugettext as _

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1

class ItemAdmin(admin.ModelAdmin):	   
	inlines = [PhoneInline]
	prepopulated_fields = {"slug": ("name",)}
	list_display = [
		"name",
		"category",
		"visits",
		"show",
		]

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Tag)
