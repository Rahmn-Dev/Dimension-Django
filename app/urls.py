from django.urls import path, include
from .views import knapsack_form, item_form, container_form, truck_form, item_form_delete, container_form_delete, truck_form_delete, dashboard, edititem_form, editContainer_form, editTruck_form
from . import api
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.shortcuts import redirect
from rest_framework import routers
from django.contrib import admin


from django.urls import path, reverse_lazy

router = routers.DefaultRouter()
router.register("item", api.ItemApiViewSet)
router.register("container", api.ContainerApiViewSet)
router.register("truck", api.TruckApiViewSet)


urlpatterns = [
    path("api/v2/", include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('kalkulasi/', knapsack_form, name='knapsack_form'),
    
    path('accounts/profile/', lambda request: redirect('dashboard'), name='root_redirect'),
    path('', dashboard, name='dashboard'),
    # path('knapsack/result/', knapsack_result, name='knapsack_result'),
    path('knapsack/item/', item_form, name='item_form'),
    path('knapsack/item/edit/<int:pk>/', edititem_form, name='item_form_edit'),
    path('knapsack/item/delete/<int:pk>/', item_form_delete, name='item_form_delete'),
    path('knapsack/container/', container_form, name='container_form'),
    path('knapsack/container/edit/<int:pk>/', editContainer_form, name='container_form_edit'),
    path('knapsack/container/delete/<int:pk>/', container_form_delete, name='container_form_delete'),
    path('knapsack/truck/', truck_form, name='truck_form'),
    path('knapsack/truck/edit/<int:pk>/', editTruck_form, name='truck_form_edit'),
    path('knapsack/truck/delete/<int:pk>/', truck_form_delete, name='truck_form_delete'),
   
]
