
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

ratios = []
for i in items:
    ratio = items[i]["calories"] / items[i]["cost"]
    ratios.append(round(ratio, 2))

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.keys(), key=lambda x: ratios[list(items.keys()).index(x)], reverse=True)
    result = []
    for item in sorted_items:
        if items[item]["cost"] <= budget:
            result.append(item)
            budget -= items[item]["cost"]
    return result

def dynamic_algorithm(items, budget):
    n = len(items)
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items[list(items.keys())[i - 1]]["cost"] <= w:
                K[i][w] = max(items[list(items.keys())[i - 1]]["calories"] + K[i - 1][w - items[list(items.keys())[i - 1]]["cost"]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    result_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if K[i][j] != K[i - 1][j]:
            result_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    return result_items, K[n][budget]

budget = 100

print("\nGreedy result:")
print("Items:", greedy_algorithm(items, budget))
print("Total calories:", sum([items[i]["calories"] for i in greedy_algorithm(items, budget)]))
print("Total cost:", sum([items[i]["cost"] for i in greedy_algorithm(items, budget)]))

dynamic_result_items, dynamic_result_calories = dynamic_algorithm(items, budget)
print("\nDynamic result:")
print("Items:", dynamic_result_items)
print("Total calories:", dynamic_result_calories)
print("Total cost:", sum([items[i]["cost"] for i in dynamic_result_items]))
