from django.contrib import admin
from bank.models import BankDetails
# Register your models here.

#register the BankDetails model : more info : goto bank/models.py
admin.site.register(BankDetails)
