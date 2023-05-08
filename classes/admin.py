from django.contrib import admin

from .models import Class, Schedule, Enrollment


class ScheduleInline(admin.TabularInline):
    model = Schedule


class EnrollmentInline(admin.TabularInline):
    model = Enrollment


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'teacher', 'start_time', 'end_time')
    inlines = [ScheduleInline, EnrollmentInline]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('class_obj', 'day_of_week', 'start_time', 'end_time')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_obj')
