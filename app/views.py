from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm, ContainerForm, KnapsackForm, TruckForm
from .utils import knapsack_greedy_algorithm
from .models import Item, Container, Truck
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

@login_required
def dashboard(request):
    items = Item.objects.all()
    containers = Container.objects.all()
    trucks = Truck.objects.all()
    
    return render(request, 'dashboard.html', {'items': items, 'containers': containers, 'trucks': trucks})

@login_required
def item_form(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_form')

    items = Item.objects.all()
    return render(request, 'item/item_form.html', {'form': ItemForm(), 'items': items})

@login_required
def item_form_delete(request, pk):
    item = Item.objects.get(pk= pk)
    item.delete()
    return HttpResponseRedirect(reverse('dashboard'))
    # instance = get_object_or_404(Item, pk=pk)

    # if request.method == 'POST':
    #     instance.delete()
    #     return redirect('item_form') 

    # return render(request, 'item/item_delete_form.html', {'instance': instance})

@login_required
def container_form(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('container_form')

    containers = Container.objects.all()
    return render(request, 'container/container_form.html', {'form': ContainerForm(), 'containers': containers})

@login_required
def container_form_delete(request, pk):
    container = Container.objects.get(pk= pk)
    container.delete()
    return HttpResponseRedirect(reverse('dashboard'))
    # instance = get_object_or_404(Container, pk=pk)

    # if request.method == 'POST':
    #     instance.delete()
    #     return redirect('container_form') 

    # return render(request, 'container/container_delete_form.html', {'instance': instance})

@login_required
def truck_form(request):
    trucks = Truck.objects.all()
    if request.method == 'POST':
        form = TruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('truck_form')
    else:
        form = TruckForm()
    return render(request, 'truck/truck_form.html', {'form': form, 'trucks': trucks})

@login_required
def truck_form_delete(request, pk):
    truck = Truck.objects.get(pk= pk)
    truck.delete()
    return HttpResponseRedirect(reverse('dashboard'))
    # instance = get_object_or_404(Truck, pk=pk)

    # if request.method == 'POST':
    #     instance.delete()
    #     return redirect('truck_form') 

    # return render(request, 'truck/truck_delete_form.html', {'instance': instance})

@login_required
def knapsack_form(request):
    form = KnapsackForm(request.POST)
    if form.is_valid():
        container = form.cleaned_data['container']
        items = Item.objects.all()
        selected_items, selected_container = knapsack_greedy_algorithm(items, container)
        
        selected_truck = None
        for truck in Truck.objects.all():
            if truck.capacity_weight >= sum(item.weight for item in selected_items):
                selected_truck = truck
                break
            
        total_value = sum(item.value for item in selected_items)
        total_price = sum(item.price for item in selected_items)


        return render(request, 'results.html', {
            'selected_items': selected_items,
            'selected_container': selected_container,
            'total_value': total_value,
            'total_price': total_price,
            'selected_truck': selected_truck,
        })

    return render(request, 'knapsack_form.html', {'form': form})

# def knapsack_result(request):
#     container = Container.objects.get(pk=1)  # Ganti dengan mekanisme pemilihan container yang sesuai
#     items = Item.objects.all()
#     selected_items, selected_container = knapsack_greedy_algorithm(items, container)

#     return render(request, 'results.html', {'selected_items': selected_items, 'selected_container': selected_container})
