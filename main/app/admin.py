from django.contrib import admin
from main.app.models import UserProfile

register = admin.site.register

register(UserProfile)
