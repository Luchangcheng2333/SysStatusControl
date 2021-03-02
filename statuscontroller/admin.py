from django.contrib import admin
from .models import Projects


# Register your models here.
@admin.register(Projects)
class controller(admin.ModelAdmin):
    list_display = ('name', 'owner', 'host_id', 'host_ip', 'OS', 'description', 'start_time', \
                    'time', 'end_time', 'analysis_status', 'result_description')
