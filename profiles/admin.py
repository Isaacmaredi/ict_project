from django.contrib import admin
from .models import Profile

class ProfileAdmin (admin.ModelAdmin):
    list_display = ['user','birth_date','unit',
                    'position','office_ext','mobile',
                    'speed_dial']
    list_display_links = ('user',)
    list_filter = ('unit',)
    search_fields = ('user',)
    list_per_page = 10
    
admin.site.register(Profile, ProfileAdmin)
    




