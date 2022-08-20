from django.contrib import admin
from app.models import Offer, Respond, Profile, User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Offer)
admin.site.register(Respond)
