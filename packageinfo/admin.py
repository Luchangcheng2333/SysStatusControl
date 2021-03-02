from django.contrib import admin
from .models import Package


# Register your models here.
@admin.register(Package)
class packagecontroller(admin.ModelAdmin):
    list_display = ('full_name', 'version', 'test_tool', 'language', 'description', 'start_time',
                    'time', 'end_time', 'analysis_status', 'result_description')
