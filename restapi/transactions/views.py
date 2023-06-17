from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Transaction
from django.contrib import messages
from django.shortcuts import render, redirect
from users.models import Profile
# Create your views here.
class TransactionListView(ListView):
    model=Transaction
    #template_name='transactions/transaction_list.html' #<app>/<model>_<viewtype>.html 
    context_object_name='transactions'
    ordering=['-date_time']
    paginate_by=5

class TransactionDetailView(DetailView):
    model=Transaction
    template_name='transactions/transaction_detail.html'

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model=Transaction
    fields=['receiver','amount']
    template_name='transactions/transaction_form.html' #<app>/<model>_<viewtype>.html
    def form_valid(self, form):
        form.instance.sender=self.request.user
        if int(self.request.user.profile.amount)<int(self.request.POST['amount']):
            messages.warning(self.request, f'Insufficient balance in your account')
            return redirect('transaction-create')
        elif self.request.user.username==self.request.POST['receiver']:
            messages.warning(self.request, f'You cannot send money to yourself')
            return redirect('transaction-create')
        elif not Profile.objects.filter(user__username=self.request.POST['receiver']).exists():
            messages.warning(self.request, f'Username of receiver does not exist')
            return redirect('transaction-create')
        else:
            return super().form_valid(form)

        
