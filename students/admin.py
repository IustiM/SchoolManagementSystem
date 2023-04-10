from django.contrib import admin

from .models import Student, Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'is_present')


admin.site.register(Student)
admin.site.register(Attendance)
