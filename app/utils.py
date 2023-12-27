# def knapsack_greedy_algorithm(items, containers, capacity):
#     containers_list = list(containers)
#     containers_list.sort(key=lambda x: x.capacity, reverse=True)

#     total_price = 0
#     selected_items = []
#     selected_container = None

#     for container in containers_list:
#         total_weight = 0
#         current_selected_items = []

#         for item in items:
#             if total_weight + item.weight <= container.capacity:
#                 total_weight += item.weight
#                 current_selected_items.append(item)
#                 total_price += item.price

#         if not selected_items or total_price > sum(item.price for item in selected_items):
#             selected_items = current_selected_items
#             selected_container = container.name

#     return total_price, selected_items, selected_container

# update
# def knapsack_greedy_algorithm(items, containers, capacity):
#     print(f"Kapasitas Kantong yang Digunakan: {capacity}")
#     containers_list = list(containers)
#     containers_list.sort(key=lambda x: x.capacity, reverse=True)

#     selected_containers = {}

#     for container in containers_list:
#         total_weight = 0
#         current_selected_items = []

#         for item in items:
#             if total_weight + item.weight <= container.capacity:
#                 total_weight += item.weight
#                 current_selected_items.append(item)

#         total_price = sum(item.price for item in current_selected_items)

#         selected_containers[container.name] = {
#             'items': current_selected_items,
#             'total_price': total_price,
#         }

#     return selected_containers

# app/utils.py
def knapsack_greedy_algorithm(items, container):
    selected_items = []
    remaining_capacity_weight = container.capacity_weight
    remaining_capacity_length = container.capacity_length
    remaining_capacity_width = container.capacity_width

    sorted_items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)

    for item in sorted_items:
        if (
            item.weight <= remaining_capacity_weight
            and item.length <= remaining_capacity_length
            and item.width <= remaining_capacity_width
        ):
            selected_items.append(item)
            remaining_capacity_weight -= item.weight
            remaining_capacity_length -= item.length
            remaining_capacity_width -= item.width

    return selected_items, container




def knapsack_dynamic_programming(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            weight_i = items[i - 1].weight
            value_i = items[i - 1].price

            if weight_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + value_i)
            else:
                dp[i][w] = dp[i - 1][w]

    total_price = dp[n][capacity]
    selected_items = []

    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1].weight

    return total_price, selected_items
