"""Definiuje wzorce adresów URL dla learning_logs."""

from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    # Strona główna
    re_path(r'^$', views.index, name='index'),

    # Wyświetlanie wszystkich tematów
    re_path(r'^topics/$', views.topics, name='topics'),

    # Strona szczegółowa dotycząca pojedynczego tematu
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]