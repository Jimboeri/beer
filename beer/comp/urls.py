from django.urls import path, include
from django.conf.urls import url

from . import views

app_name='comp'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('player/<int:player_id>/', views.playerDets, name='playerDets'),
]