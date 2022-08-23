from django.contrib import admin
from .models import Country,Employee,Location, Place,Salary


class CountryAdmin(admin.ModelAdmin):
       list_display = ('name','country_code',)
       search_fields=("name",'country_code',)
       list_filter=('name','country_code',)



admin.site.register(Country,CountryAdmin)
admin.site.register(Employee)
admin.site.register(Location)
admin.site.register(Salary)
admin.site.register(Place)

