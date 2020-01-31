from django.contrib import admin

#Register your models here.
from .models import Idol, Video

class IdolAdmin(admin.ModelAdmin):
   list_display = ('name', 'birthday')
   
admin.site.register(Idol, IdolAdmin)
admin.site.register(Video)
