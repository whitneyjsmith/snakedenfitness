# Generated by Django 4.1.1 on 2022-10-31 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0003_alter_meal_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='name',
            new_name='meal_name',
        ),
    ]
