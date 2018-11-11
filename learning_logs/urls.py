"""Definiuje wzorce adresów URL dla learning_logs."""

from django.urls import re_path
from . import views

urlpatterns = [
    # Strona główna
    re_path(r'^$', views.index, name='index'),

    # Wyświetlanie wszystkich tematów
    re_path(r'^topics/$', views.topics, name='topics'),

    # Strona szczegółowa dotycząca pojedynczego tematu
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Strona przeznaczona do dodawania nowego tematu
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Strona przeznaczona do dodawania nowego wpisu
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Strona przeznaczona do edycji wpisu
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]