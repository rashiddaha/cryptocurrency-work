from .traders_account import TraderAccounts
from django.db import models


class KucoinPassword(models.Model):
    trader_account = models.OneToOneField(TraderAccounts, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)