from django.contrib import admin
from test_app.models import SportData,EntertainData,Polity
from test_app.models import SportExten,EntertainExten,PolityExten
from test_app.models import LatestData,LatestExten
# Register your models here.

class LatestDataAdmin(admin.ModelAdmin):
    list_display = ['title','image','url']
class LatestExtenAdmin(admin.ModelAdmin):
    list_display = ['title','url']

admin.site.register(LatestData,LatestDataAdmin)
admin.site.register(LatestExten,LatestExtenAdmin)



class SportDataAdmin(admin.ModelAdmin):
    list_display = ['title','image','url']
class SportExtenAdmin(admin.ModelAdmin):
    list_display = ['title','url']

admin.site.register(SportData,SportDataAdmin)
admin.site.register(SportExten,SportExtenAdmin)

class EntertainDataAdmin(admin.ModelAdmin):
    list_display = ['title','image','url']
class EntertainExtenAdmin(admin.ModelAdmin):
    list_display = ['title','url']

admin.site.register(EntertainData,EntertainDataAdmin)
admin.site.register(EntertainExten,EntertainExtenAdmin)


class PolityAdmin(admin.ModelAdmin):
    list_display = ['title','image','url']
class PolityExtenAdmin(admin.ModelAdmin):
    list_display = ['title','url']

admin.site.register(Polity,PolityAdmin)
admin.site.register(PolityExten,PolityExtenAdmin)
