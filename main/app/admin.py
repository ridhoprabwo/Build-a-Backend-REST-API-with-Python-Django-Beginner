from django.contrib import admin
from main.app.models import UserProfile, ProfileFeedItem

register = admin.site.register

register(UserProfile)
register(ProfileFeedItem)
