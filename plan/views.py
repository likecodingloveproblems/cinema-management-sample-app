from django import views
from django.http import HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from plan.models import Room, Movie, Schedule, Seat, Ticket
# Create your views here.

class RoomView(views.View):
    template_name = 'rooms.html'
    def get(self, request):
        rooms = Room.objects.all()
        context = {
            'title': 'Rooms',
            'rooms': rooms
        }
        return render(request, self.template_name, context)

class ScheduleView(views.View):
    template_name = 'schedules.html'
    def get(self, request, *args, **kwargs):
        room_id = kwargs['room_id']
        room = get_object_or_404(Room, pk=room_id)
        schedules = Schedule.objects.filter(room_id=room_id)
        context = {
            'room': room,
            'schedules': schedules
        }
        return render(request, self.template_name, context)

class SeatView(views.View):
    template_name = 'seats.html'
    
    def get_context_data(self, **kwargs):
        schedule_id = kwargs['schedule_id']
        schedule = get_object_or_404(Schedule, pk=schedule_id)
        movie = get_object_or_404(Movie, pk=schedule.movie.id)
        room = get_object_or_404(Room, pk=schedule.room.id)
        seats = Seat.objects.get_room_seats(room=room)
        context = {
            'schedule': schedule,
            'room': room,
            'movie': movie,
            'date_time': schedule.date_time,
            'seats': seats
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # get seat by seat_id
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, pk = seat_id)
        # it's better to validate it in forms or model not in view
        if Ticket.objects.filter(seat = seat, schedule_id = context['schedule']):
            return HttpResponseBadRequest('some thing went wrong, it seems client edited html :(')
        Ticket.objects.purchase(request.user, context['schedule'], seat)
        return render(request, self.template_name, context)