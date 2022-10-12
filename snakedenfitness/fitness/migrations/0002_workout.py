# Generated by Django 4.1.1 on 2022-10-10 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_type', models.CharField(max_length=50)),
                ('muscle_group', models.CharField(max_length=50)),
                ('exercise_name', models.CharField(max_length=50)),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
