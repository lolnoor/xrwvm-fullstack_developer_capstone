from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline clas
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 2
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'type', 'year']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]
    
    
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
