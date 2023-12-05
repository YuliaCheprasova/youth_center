from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('helper/', helper, name="helper"),
    path('curr_events/', Current.as_view(), name="current"),
    path('archive/', Archive.as_view(), name="archive"),
    path('event/<slug:event_slug>/', ShowEvent.as_view(), name="show_event"),
    path('add_event/', AddEvent.as_view(), name="add_event"),
    path('event/<slug:event_slug>/edit/', EventEdit.as_view(), name='event_edit'),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('delete_event/<slug:event_slug>/', EventDelete.as_view(), name="delete_event"),
    path('plan/', plan, name="plan"),
    path('tz/', tz, name="tz"),
    path('estimates/', estimates, name="estimates"),
    path('sz/', sz, name="sz"),
    path('report/', report, name="report"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

