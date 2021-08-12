from django.contrib import admin

# Register your models here.
from .models import Car, Tint, TintTask



class TintTaskAdmin(admin.ModelAdmin):    

    def get_changeform_initial_data(self, request):
        get_data = super(TintTaskAdmin, self).get_changeform_initial_data(request)
        get_data['tinter'] = request.user.pk
        return get_data

class TaskInline(admin.TabularInline):    
    model = TintTask

class CarAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


admin.site.register(Car, CarAdmin)
admin.site.register(Tint)
admin.site.register(TintTask, TintTaskAdmin)
