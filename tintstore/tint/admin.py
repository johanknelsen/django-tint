from django.contrib import admin

# Register your models here.
from .models import Car, Tint, TintTask

admin.site.register(Car)
admin.site.register(Tint)
admin.site.register(TintTask)