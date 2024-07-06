from django.db import models

# Create your models here.
class Income(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=200)

# class Categories(models.Model):
    

class Transactions(models.Model):
    amount = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=500)
    category_Choices = {
        "Groceries": "Groceries",
        "Food": "Food",
        "Entertainment": "Entertainment",
        "Gas": "Gas",
        "Housing": "Housing",
        "Transportation": "Transportation",
        "Health": "Health",
        "Debt": "Debt",
        "Education": "Education",
        "Savings": "Savings",
        "Investments": "Investments",
        "Misc": "Misc"
    }

class Goals(models.Model):
    goal_name = models.CharField(max_length=100)
    target_amount = models.IntegerField()
    target_date = models.DateField()
    notes = models.CharField(max_length=250)

class Reports(models.Model):
    total_income = models.IntegerField()
    total_expenses = models.IntegerField()

class Reminders(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.CharField(max_length=250)