# Generated by Django 4.1.2 on 2022-12-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_picture', models.FileField(upload_to='')),
            ],
        ),
    ]