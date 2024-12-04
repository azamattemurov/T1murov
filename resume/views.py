import os
from django.http import FileResponse, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Song
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Song
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy

app_name = 'resume'


class HomePageView(TemplateView):
    template_name = 'index-one.html'


class SongListView(ListView):
    model = Song
    template_name = 'songs-one.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.all()


class SongDownloadView(View):
    def get(self, request, *args, **kwargs):
        song = Song.objects.get(pk=kwargs['pk'])
        # Download hisobini oshirish
        song.download_count += 1
        song.save()

        # Foydalanuvchiga faylni yuborish
        response = HttpResponse(song.audio_file, content_type='audio/mp3')
        response['Content-Disposition'] = f'attachment; filename="{song.song_name}.mp3"'
        return response


class AboutOneView(TemplateView):
    template_name = 'about-one.html'


class ContactTemplateView(FormView):
    template_name = 'contact-one.html'
    form_class = ContactForm
    success_url = reverse_lazy('resume:success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(
            'Sizga taklifim bor!',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,
            ['sotvoldiyevazamat193@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'succes.html'
