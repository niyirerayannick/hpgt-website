from django.urls import path
from django.views import defaults as default_views
from core import views

urlpatterns = [
    path('', views.index, name='home'),
    path('what-we-do', views.service, name='service'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    path('who-we-are/our-management-team', views.team_list, name='team'),
    path('who-we-are/vision-mission-and-values', views.vmv, name='vision-mission-and-values'),
    path('who-we-are/belives', views.belives, name='belives'),
    path('become-volunteer', views.join, name='join'),
    path('our-families', views.family, name='family'),
    path('blog', views.blog, name='blog'),
    path('event-and-announcements', views.event, name='event'),
    path('contact-us', views.join, name='contact'),
  
]

