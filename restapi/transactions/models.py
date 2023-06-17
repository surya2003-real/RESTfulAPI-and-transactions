from django.db import models
from users.models import Profile
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect

# Create your models here.
class Transaction(models.Model):
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    amount=models.IntegerField()
    date_time=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.sender} sent {self.amount} to {self.receiver}'
    
    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk':self.pk})

    