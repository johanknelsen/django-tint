from django.contrib import admin

# Register your models here.
from .models import Car, Tint, TintTask

class CarInline(admin.TabularInline):
    model = Car

class TintTaskAdmin(admin.ModelAdmin):
    # inlines = [
    #     CarInline,
    # ]

    def get_changeform_initial_data(self, request):
        get_data = super(TintTaskAdmin, self).get_changeform_initial_data(request)
        get_data['tinter'] = request.user.pk
        return get_data

admin.site.register(Car)
admin.site.register(Tint)
admin.site.register(TintTask, TintTaskAdmin)
