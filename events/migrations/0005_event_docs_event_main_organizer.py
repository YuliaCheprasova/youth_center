# Generated by Django 4.2.5 on 2023-11-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_alter_event_data_alter_event_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="docs",
            field=models.URLField(
                null=True, verbose_name="Ссылка на диск с файлами мероприятия"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="main_organizer",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Руководитель"
            ),
        ),
    ]