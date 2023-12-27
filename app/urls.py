from django.urls import path
from .views import knapsack_form, item_form, container_form, truck_form, item_form_delete, container_form_delete, truck_form_delete
urlpatterns = [
    path('', knapsack_form, name='knapsack_form'),
    # path('knapsack/result/', knapsack_result, name='knapsack_result'),
    path('knapsack/item/', item_form, name='item_form'),
    path('knapsack/item/edit/<int:pk>/', item_form, name='item_form_edit'),
    path('knapsack/item/delete/<int:pk>/', item_form_delete, name='item_form_delete'),
    path('knapsack/container/', container_form, name='container_form'),
    path('knapsack/container/edit/<int:pk>/', item_form, name='container_form_edit'),
    path('knapsack/container/delete/<int:pk>/', container_form_delete, name='container_form_delete'),
    path('knapsack/truck/', truck_form, name='truck_form'),
    path('knapsack/truck/edit/<int:pk>/', item_form, name='truck_form_edit'),
    path('knapsack/truck/delete/<int:pk>/', truck_form_delete, name='truck_form_delete'),
   
]
