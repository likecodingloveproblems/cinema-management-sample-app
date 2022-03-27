# Generated by Django 4.0.3 on 2022-03-24 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='name')),
                ('poster', models.ImageField(upload_to=None, verbose_name='poster')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='movie date time')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.movie', verbose_name='movie')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.room', verbose_name='room')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_id', models.IntegerField(verbose_name='seat_id')),
                ('row', models.IntegerField(verbose_name='row')),
                ('column', models.IntegerField(verbose_name='column')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.room', verbose_name='room')),
            ],
            options={
                'verbose_name': 'Seat',
                'verbose_name_plural': 'Seats',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='buyyer')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.schedule', verbose_name='schedule')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.seat', verbose_name='seat')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='movies',
            field=models.ManyToManyField(related_name='movies', through='plan.Schedule', to='plan.movie', verbose_name='movies'),
        ),
    ]