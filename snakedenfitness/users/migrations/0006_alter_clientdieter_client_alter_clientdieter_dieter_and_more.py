# Generated by Django 4.0 on 2022-12-07 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0005_alter_clientdieter_client_alter_clientdieter_dieter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdieter',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='D_assigned_client', to='auth.user', unique=True),
        ),
        migrations.AlterField(
            model_name='clientdieter',
            name='dieter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='D_assigned_dietician', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='clienttrainer',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_assigned_client', to='auth.user', unique=True),
        ),
        migrations.AlterField(
            model_name='clienttrainer',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_assigned_trainer', to='auth.user'),
        ),
    ]
