# knapsack_app/views.py
from django.shortcuts import render
from .forms import KnapsackForm
from .models import Item

def knapsack_greedy(request):
    if request.method == 'POST':
        form = KnapsackForm(request.POST)
        if form.is_valid():
            capacity = form.cleaned_data['capacity']
            num_items = form.cleaned_data['num_items']
            
            # Mengambil data barang dari form
            items_data = []
            for i in range(num_items):
                name = form.cleaned_data[f'name_{i}']
                price = form.cleaned_data[f'price_{i}']
                weight = form.cleaned_data[f'weight_{i}']

                # Membuat instance Item dari data
                item = Item(name=name, price=price, weight=weight)
                items_data.append(item)
            
            # Sekarang Anda memiliki data barang yang dapat diproses
            # Lanjutkan dengan implementasi algoritma knapsack
            total_price, selected_items = knapsack_greedy_algorithm(items_data, capacity)

            return render(request, 'results.html', {'selected_items': selected_items, 'total_price': total_price})

    else:
        form = KnapsackForm()

    return render(request, 'knapsack_form.html', {'form': form})



# knapsack_app/views.py
def knapsack_greedy_algorithm(items, capacity):
    items.sort(key=lambda x: x.price / x.weight, reverse=True)

    total_price = 0
    total_weight = 0
    selected_items = []

    for item in items:
        if total_weight + item.weight <= capacity:
            total_price += item.price
            total_weight += item.weight
            selected_items.append(item)

    return total_price, selected_items
