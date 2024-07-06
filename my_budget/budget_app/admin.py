from django.contrib import admin
from .models import Income, Transactions, Goals, Reminders, Reports


admin.site.register(Income)
admin.site.register(Transactions)
admin.site.register(Goals)
admin.site.register(Reminders)
admin.site.register(Reports)

# Register your models here.
