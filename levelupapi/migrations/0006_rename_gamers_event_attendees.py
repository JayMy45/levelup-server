# Generated by Django 4.1.2 on 2022-11-07 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0005_remove_gamer_events_event_gamers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='gamers',
            new_name='attendees',
        ),
    ]