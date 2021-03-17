from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.

class fadmin (admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class padmin (admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Flight, fadmin)
admin.site.register(Airport)
admin.site.register(Passenger, padmin)