from django.contrib import admin

from .models import Teacher, Attendance, Course, Schedule


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'date', 'is_present')


admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(Course)
admin.site.register(Schedule)
