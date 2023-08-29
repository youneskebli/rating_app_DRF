from django.contrib import admin
from .models import Rating,Phone

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'user', 'stars']
    list_filter = ['user','phone']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(Rating,RatingAdmin)
admin.site.register(Phone,PhoneAdmin)