# Generated by Django 4.0.5 on 2022-06-29 08:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_bar_rate_alter_drink_rate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bar',
            new_name='Pub',
        ),
    ]
