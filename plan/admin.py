from django.contrib import admin
from plan.models import Movie, Room, Schedule
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
