from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Goals, Reminders, Reports, Transactions, Income


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class GoalList(TemplateView):
    template_name = "goals.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Goals"] = Goals.objects.all() # Here we are using the model to query the database for us.
        return context