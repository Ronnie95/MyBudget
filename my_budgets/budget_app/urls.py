from django.urls import path
from . import views
# from .models import Goals, Reminders, Reports, Transactions, Income

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('goal/', views.GoalList.as_view(), name="goals"), # <- here we have added the new path
    path('goal/new/', views.GoalCreate.as_view(), name ='goal_create'),
    path('goal/<int:pk>/', views.GoalDetail.as_view(), name='goal_detail'),
    path('goal/<int:pk>/update', views.GoalUpdate.as_view(), name='goal_update'),
    path('goal/<int:pk>/delete', views.GoalDelete.as_view(), name='goal_delete'),

    path('accounts/signup/', views.Signup.as_view(), name="signup")

]