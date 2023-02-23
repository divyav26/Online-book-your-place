from django.contrib import admin
from .models import State,Place,LineItem,Customer
admin.site.register(Customer)
admin.site.register(State)
admin.site.register(LineItem)
# admin.site.register(Customer)
class AdminPlace(admin.ModelAdmin):
    list_display=('title','category','add_time')

admin.site.register(Place,AdminPlace)
