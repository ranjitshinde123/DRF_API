# Generated by Django 4.0.5 on 2022-10-11 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_is_verify'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motp_counter', models.IntegerField(default=0)),
                ('motp_timer', models.DateTimeField(default=django.utils.timezone.now)),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Demo',
        ),
    ]
