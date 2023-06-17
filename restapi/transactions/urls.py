from django.urls import path
from .views import TransactionListView, TransactionDetailView, TransactionCreateView
urlpatterns = [
    path('', TransactionListView.as_view(), name='transactions'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('new/', TransactionCreateView.as_view(), name='transaction-create'),
]