from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePgWiew(TemplateView):
    template_name = "home.html"

class AbautWiew(TemplateView):
    template_name = "abaut.html"



def homePageView(request):
    return HttpResponse("hello word!")
