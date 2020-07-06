from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class Adminprofile(admin.ModelAdmin):
    list_display=('id','name','email','password')
