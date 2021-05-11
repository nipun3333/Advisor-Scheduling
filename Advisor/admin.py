from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Advisor)
admin.site.register(models.Booking)
# Register your models here.
