from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Goals, Reminders, Reports, Transactions, Income
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class GoalCreate(CreateView):
    model = Goals
    fields = ['goal_name', 'target_amount', 'target_date', 'notes']
    template_name = "goal_create.html"
    success_url = "/goals/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GoalCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('goal_detail', kwargs={'pk': self.object.pk})


class MovieDetail(DetailView):
    model = Goals
    template_name = "goal_detail.html"



class GoalList(TemplateView):
    template_name = "goals.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Goals"] = Goals.objects.all() # Here we are using the model to query the database for us.
        return context