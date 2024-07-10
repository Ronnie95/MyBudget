from django.urls import path
from . import views
# from .models import Goals, Reminders, Reports, Transactions, Income

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('goals/', views.GoalList.as_view(), name="goals"), # <- here we have added the new path
    path('goals/new/', views.GoalCreate.as_view(), name ='goal_create'),
    path('accounts/signup/', views.Signup.as_view(), name="signup")

]