from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название мероприятия")
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")
    data = models.DateTimeField(blank=True, verbose_name="Дата проведения", null=True)
    place = models.CharField(max_length = 255, verbose_name="Место проведения", null=True, blank=True)
    poster = models.ImageField(upload_to="posters/", null=True, verbose_name="Афиша", blank=True)
    description = models.TextField(blank=True, verbose_name="Описание мероприятия")
    main_organizer = models.CharField(max_length=255, null=True, verbose_name="Руководитель")
    organizers = models.TextField(verbose_name="Организаторы")
    docs = models.URLField(blank=True, null=True, verbose_name="Ссылка на диск с файлами мероприятия")
    is_done = models.BooleanField(default=False, verbose_name="Прошедшее мероприятие")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('show_event', kwargs={'event_slug': self.slug})
    class Meta:
        ordering = ['-data',]

