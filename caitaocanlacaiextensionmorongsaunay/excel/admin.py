from django.contrib import admin

from .models import dictionary as City

class CityAdmin(admin.ModelAdmin):
    list_display = ("Eng", "Viet", "pronunciation",)

admin.site.register(City, CityAdmin)
