from django.urls import path

from resume import views
from resume.views import HomePageView, ContactTemplateView, SongListView, SongDownloadView, AboutOneView, ThankYouView
app_name = 'resume'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', views.AboutOneView.as_view(), name='about'),
    path('songs/', views.SongListView.as_view(), name='songs'),
    path('songs/<int:pk>/', views.SongDownloadView.as_view(), name='songs_download'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('success/',ThankYouView.as_view(), name='success'),


]