from django.contrib.sitemaps import Sitemap
from .models import Room, Topic  # Import your models here

from .models import User  # Import your User model here

class UserSitemap(Sitemap):
    def items(self):
        return User.objects.all()  # Return the list of users

    def lastmod(self, obj):
        return obj.last_modified  # Assuming the User model has a 'last_modified' field

class RoomSitemap(Sitemap):
    def items(self):
        return Room.objects.all()  # Returns all rooms in your database

    def lastmod(self, obj):
        return obj.updated_at  # You can use any field that indicates the last time the room was updated


class TopicSitemap(Sitemap):
    def items(self):
        return Topic.objects.all()  # Return all topics

    def lastmod(self, obj):
        return obj.updated_at  # Use an appropriate field to determine the last modified time
