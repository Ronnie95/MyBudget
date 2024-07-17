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
    path('reminders/', views.ReminderList.as_view(), name="reminders"), # <- here we have added the new path
    path('reminders/new/', views.ReminderCreate.as_view(), name ='reminder_create'),
    path('reminders/<int:pk>/', views.ReminderDetail.as_view(), name='reminder_detail'),
    path('reminders/<int:pk>/update', views.ReminderUpdate.as_view(), name='reminder_update'),
    path('reminders/<int:pk>/delete', views.ReminderDelete.as_view(), name='reminder_delete'),
    path('transactions/', views.TransactionList.as_view(), name="transaction"), # <- here we have added the new path
    path('transactions/new/', views.TransactionCreate.as_view(), name ='transactions_create'),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transactions_detail'),
    path('transactions/<int:pk>/update/', views.TransactionUpdate.as_view(), name='transactions_update'),
    path('transactions/<int:pk>/delete', views.TransactionDelete.as_view(), name='transactions_delete'),
    path('income/', views.IncomeList.as_view(), name="income_list"), # <- here we have added the new path
    path('income/new/', views.IncomeCreate.as_view(), name ='income_create'),
    path('income/<int:pk>/', views.IncomeDetail.as_view(), name='income_detail'),
    path('income/<int:pk>/update/', views.IncomeUpdate.as_view(), name='income_update'),
    path('income/<int:pk>/delete', views.IncomeDelete.as_view(), name='income_delete'),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]