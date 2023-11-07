from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .forms import *

from .models import *


def index(request):
    return render(request, 'events/index.html', {'title': 'Молодежный центр'})


def helper(request):
    return render(request, 'events/helper.html', {'title': 'Помощник организатора'})


def current(request):
    all_events = Event.objects.filter(is_done=False)
    paginator = Paginator(all_events, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/listevents.html', {'page_obj': page_obj, 'all_events': all_events, 'title': 'Текущие мероприятия'})


def archive(request):
    all_events = Event.objects.filter(is_done=True)
    paginator = Paginator(all_events, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/listevents.html', {'page_obj': page_obj, 'all_events': all_events, 'title': 'Архив мероприятий'})


def show_event(request,event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    return render(request, 'events/show_event.html', {'event': event, 'title': event.title})


def add_event(request):
    if request.method =='POST':
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('show_event', event_slug=event.slug)
    else:
        form = AddEventForm()
    return render(request, 'events/add_event.html', {'form': form, 'title': "Добавление мероприятия"})


def event_edit(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    if request.method == "POST":
        form = AddEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('show_event', event_slug=event.slug)
    else:
        form = AddEventForm(instance=event)
    return render(request, 'events/add_event.html', {'form': form, 'title': "Редактирование мероприятия"})