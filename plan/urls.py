from django.urls import path
from plan.views import RoomView, ScheduleView, SeatView

urlpatterns = [
    path('', RoomView.as_view(), name='rooms'),
    path('movie/<int:room_id>/', ScheduleView.as_view(), name='schedules'),
    path('seat/<int:schedule_id>/', SeatView.as_view(), name='seat'),
]
