# knapsack/urls.py
from django.urls import path
from .views import knapsack_greedy

urlpatterns = [
    path('knapsack', knapsack_greedy, name='knapsack_greedy'),
]
