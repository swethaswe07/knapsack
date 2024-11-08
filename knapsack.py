import random

def generate_knapsack_problem(n):
    items = []
    for i in range(n):
        name = "item" + str(i + 1)
        size = random.randint(1, 5)
        value = random.randint(1, 10)
        item = (name, size, value)
        items.append(item)
    return items

print(generate_knapsack_problem(5))
