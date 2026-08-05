from django.contrib import admin
from .models import ContactMessage, Itinerary
from .models import Wishlist
from .models import Profile

admin.site.register(Profile)
admin.site.register(Wishlist)

admin.site.register(ContactMessage)
admin.site.register(Itinerary)