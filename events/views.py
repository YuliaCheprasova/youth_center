from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import *

from .models import *


def index(request):
    return render(request, 'events/index.html', {'title': 'Молодежный центр'})


def helper(request):
    return render(request, 'events/helper.html', {'title': 'Помощник организатора'})


def plan(request):
    return render(request, 'events/plan.html', {'title': 'Помощник организатора'})


def estimates(request):
    return render(request, 'events/estimates.html', {'title': 'Помощник организатора'})


def sz(request):
    return render(request, 'events/sz.html', {'title': 'Помощник организатора'})


def tz(request):
    return render(request, 'events/tz.html', {'title': 'Помощник организатора'})


def report(request):
    return render(request, 'events/report.html', {'title': 'Помощник организатора'})



class Current(ListView):
    paginate_by = 3
    model = Event
    template_name = 'events/listevents.html'
    #context_object_name = 'page_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"]="Текущие мероприятия"
        return context

    def get_queryset(self):
        return Event.objects.filter(is_done=False)


"""def current(request):
    all_events = Event.objects.filter(is_done=False)
    paginator = Paginator(all_events, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/listevents.html', {'page_obj': page_obj, 'all_events': all_events, 'title': 'Текущие мероприятия'})"""


class Archive(ListView):
    paginate_by = 3
    model = Event
    template_name = 'events/listevents.html'
    #context_object_name = 'page_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"]="Архив мероприятий"
        return context

    def get_queryset(self):
        return Event.objects.filter(is_done=True)


"""def archive(request):
    all_events = Event.objects.filter(is_done=True)
    paginator = Paginator(all_events, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/listevents.html', {'page_obj': page_obj, 'all_events': all_events, 'title': 'Архив мероприятий'})"""


class ShowEvent(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/show_event.html'
    slug_url_kwarg = 'event_slug'
    #redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']=context['event']
        return context


"""def show_event(request,event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    return render(request, 'events/show_event.html', {'event': event, 'title': event.title})"""


class AddEvent(CreateView):
    form_class = AddEventForm
    template_name = 'events/add_event.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Добавление мероприятия"
        return context


"""def add_event(request):
    if request.method =='POST':
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('show_event', event_slug=event.slug)
    else:
        form = AddEventForm()
    return render(request, 'events/add_event.html', {'form': form, 'title': "Добавление мероприятия"})
"""


class EventEdit(UpdateView):
    model = Event
    form_class = AddEventForm
    template_name = 'events/add_event.html'
    slug_url_kwarg = 'event_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование мероприятия"
        return context

"""def event_edit(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    if request.method == "POST":
        form = AddEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('show_event', event_slug=event.slug)
    else:
        form = AddEventForm(instance=event)
    return render(request, 'events/add_event.html', {'form': form, 'title': "Редактирование мероприятия"})"""


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'events/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"]="Регистрация"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class=LoginUserForm
    template_name = 'events/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"]="Авторизация"
        return context

    #def get_success_url(self):
        #return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class EventDelete(DeleteView):
    model = Event
    template_name = 'events/show_event.html'
    success_url = reverse_lazy('current')
    slug_url_kwarg = 'event_slug'


def count_score(request):
    result = None

    if request.method == 'POST':
        form = MathForm(request.POST)

        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            number3 = form.cleaned_data['number3']
            number4 = form.cleaned_data['number4']
            number5 = form.cleaned_data['number5']
            number6 = form.cleaned_data['number6']
            result = 4*number1 + 3*number2 + 2*number3 + 2*number4 + 1.5*number5 + 1*number6

    else:
        form = MathForm()

    return render(request, 'events/score.html', {'title': 'Подсчет баллов ПГАС', 'form': form, 'result': result})
