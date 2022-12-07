# Generated by Django 4.0 on 2022-12-07 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('diet', '0003_delete_dietitianprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientDieter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_diet_client', to='auth.user', unique=True)),
                ('dieter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_dietician', to='auth.user')),
            ],
        ),
    ]
