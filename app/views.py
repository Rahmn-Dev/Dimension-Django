from django.shortcuts import render
from .models import Item

def knapsack_greedy(request):
    if request.method == 'POST':
        capacity = int(request.POST.get('capacity'))
        items = Item.objects.all().order_by('-price')

        selected_items = []
        current_weight = 0
        total_price = 0

        for item in items:
            if current_weight + item.weight <= capacity:
                selected_items.append(item)
                current_weight += item.weight
                total_price += item.price

        context = {
            'capacity': capacity,
            'selected_items': selected_items,
            'total_price': total_price,
        }

        return render(request, 'results.html', context)

    num_items = 5  
    item_range = range(num_items)
    return render(request, 'knapsack_form.html', {'num_items': num_items, 'item_range': item_range})
