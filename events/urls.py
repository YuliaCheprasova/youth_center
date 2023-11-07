from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('helper/', helper, name="helper"),
    path('curr_events/', current, name="current"),
    path('archive/', archive, name="archive"),
    path('event/<slug:event_slug>/', show_event, name="show_event"),
    path('add_event/', add_event, name="add_event"),
    path('event/<slug:event_slug>/edit/', event_edit, name='event_edit'),
]