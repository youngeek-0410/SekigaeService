from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate, login, logout
)
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponse


def signin_callback(request):
    # TODO: improve security
    user = authenticate(request)
    login(request, user)
    return HttpResponse(reverse("session:temp_index"))


def signout(request):
    logout(request)
    return HttpResponse(reverse("session:temp_index"))


class SigninView(TemplateView):
    template_name = 'session/signin.html'


class TempIndexView(TemplateView):
    template_name = 'session/temp-index.html'
