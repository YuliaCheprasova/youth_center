# Generated by Django 4.2.5 on 2023-11-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0006_alter_event_data_alter_event_docs_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="main_organizer",
        ),
    ]