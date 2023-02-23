from django.contrib import admin
from .models import State,Place,Contact

admin.site.register(State)

class AdminPlace(admin.ModelAdmin):
    list_display=('title','category','add_time')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','contact','description']

admin.site.register(Place,AdminPlace)
