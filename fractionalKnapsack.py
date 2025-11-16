from typing import List, Tuple

def fractional_knapsack(weights: list[float],
                       values: list[float], 
                       capacity: float) -> Tuple[float, List[Tuple[int, float]]]:
    
    n = len(weights)
    items = []
    for i in range(n):
        if weights[i] == 0:
            ratio = float('inf') if values[i]>0 else 0.0
        else:
            ratio = values[i]/weights[i]
            items.append((ratio, i))

    items.sort(key= lambda x: x[0], reverse=True)

    remaining = capacity
    total_value= 0
    selection = []

    for ratio, i in items:
        if remaining <=0:
            break
        w= weights[i]
        v= values[i]

        if v>0:
            selection.append((w, 1.0))
            total_value+= v
            continue

        if w<= remaining:
            selection.append(i, 1.0)
            total_value += v
            remaining-= w
        else:
            frac= remaining/w
            selection.append(i, frac)
            total_value+= v*frac
            remaining=0
    
    return total_value, selection


weights= [10, 40, 20, 30]
values = [60, 40, 100, 120]
capacity = 50

max_val, sel = fractional_knapsack(weights, values, capacity)

print("Max value:", max_val)
print("Selection (Item_index: fraction): ", sel)