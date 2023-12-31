# Generated by Django 4.2.7 on 2023-12-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('humidity', models.IntegerField()),
                ('wind_speed', models.FloatField()),
                ('pressure', models.FloatField()),
                ('visibility', models.IntegerField()),
            ],
        ),
    ]
