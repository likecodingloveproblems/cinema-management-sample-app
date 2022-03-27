# Generated by Django 4.0.3 on 2022-03-24 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_movie_poster_alter_room_movies_alter_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='plan.seat', verbose_name='seat'),
        ),
    ]