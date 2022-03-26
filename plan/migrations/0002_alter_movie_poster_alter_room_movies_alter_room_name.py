# Generated by Django 4.0.3 on 2022-03-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movie', verbose_name='poster'),
        ),
        migrations.AlterField(
            model_name='room',
            name='movies',
            field=models.ManyToManyField(related_name='rooms', through='plan.Schedule', to='plan.movie', verbose_name='movies'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=127, unique=True, verbose_name='name'),
        ),
    ]
