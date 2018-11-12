from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    """Wylogowanie użytkownika."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
