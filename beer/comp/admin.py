from django.contrib import admin

# Register your models here.
from .models import Profile, Registration, Competition

admin.site.register(Profile)
admin.site.register(Registration)
admin.site.register(Competition)
