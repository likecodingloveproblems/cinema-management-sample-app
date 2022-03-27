from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
'''
This app is only for a specific customer and does not design as
    Software as a Service. if the commercial team want to sell it 
    to different cinemas, for each cinema we must deploy a distance of project.

Assumptions:
1- Does all seats cost same?
2- Is the seat position important to users?
3- Can operation team define each room seats?
4- Can user gift a seat to other users?
5- Can user buy many seats in one ticket or 
    he/she can buy only one seat for each ticket?
'''

class RoomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_all_store_with_schedules(self):
        return self.get_queryset().prefetch_related('schedule_set')


class Room(models.Model):

    name = models.CharField(_("name"), unique=True, max_length=127)
    movies = models.ManyToManyField(
        "plan.Movie",
        verbose_name=_("movies"),
        related_name="rooms",
        through="plan.Schedule",
        )
    objects = RoomManager()

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")

    def __str__(self):
        return self.name

class Movie(models.Model):
 
    # It seemed movies often have unique title. 
    # also if it's not correct we must create a unique barcode field for customers.
    title = models.CharField(_("name"), max_length=127, unique=True)
    poster = models.ImageField(_("poster"), upload_to='movie', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")
        constraints = [
            models.UniqueConstraint(fields=['title', 'poster'], name='unique_title'), # this will enforce new poster for each movie
        ]

    def __str__(self):
        return self.title

class Schedule(models.Model):

    room = models.ForeignKey("plan.Room", verbose_name=_("room"), on_delete=models.CASCADE)
    movie = models.ForeignKey("plan.Movie", verbose_name=_("movie"), on_delete=models.CASCADE)
    # It's not rational to schedule for past.
    date_time = models.DateTimeField(_("movie date time"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedules")
        constraints = [
            models.UniqueConstraint(fields=['room', 'date_time'], name='unique_room_datetime')
        ]

    def __str__(self):
        return f'room: {self.room}, movie: {self.movie}, date time: {self.date_time}'

class SeatManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_room_seats(self, room):
        return self.get_queryset().filter(room=room)

class Seat(models.Model):

    room = models.ForeignKey("plan.Room", verbose_name=_("room"), on_delete=models.CASCADE)
    # seat_id is not primary key because it is used by operational team and in a scenario
    # that operation team want to change seat_id for it's internal management reasons it can 
    # make issues in tickets, because customer don't take attention to id, take attention to 
    # position of seat
    seat_id = models.IntegerField(_("seat_id"))
    # we assume rooms are rectangular, for other shapes we must have other options
    row = models.IntegerField(_("row"))
    column = models.IntegerField(_("column"))
    objects = SeatManager()

    class Meta:
        verbose_name = _("Seat")
        verbose_name_plural = _("Seats")
        constraints = [
            models.UniqueConstraint(fields=['room', 'row', 'column'], name='unique_room_row_column'),
            models.UniqueConstraint(fields=['room', 'seat_id'], name='unique_room_seat_id'),
        ]

    def __str__(self):
        return f'room: {self.room}, id: {self.seat_id}'

class TicketManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def _purchase(self, user, schedule, seat):
        ticket = self.create(buyyer=user, schedule=schedule, seat=seat)
        return ticket

    def purchase(self, user, schedule, seat):
        ticket = self._purchase(user, schedule, seat)
        return ticket

class Ticket(models.Model):

    # user can play different roles: buyyer and owner, if we have gifting process we must change ticket model.
    buyyer = models.ForeignKey(User, verbose_name=_("buyyer"), on_delete=models.CASCADE)
    schedule = models.ForeignKey("plan.Schedule", verbose_name=_("schedule"), on_delete=models.CASCADE)
    seat = models.ForeignKey("plan.Seat", verbose_name=_("seat"), on_delete=models.CASCADE, related_name='ticket')
    objects = TicketManager()

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")
        constraints = [
            models.UniqueConstraint(fields=['schedule', 'seat'], name='unique_ticket')
        ]

    def __str__(self):
        return f'buyyer: {self.buyyer}, schedule: "{self.schedule}", seat: "{self.seat}"'
