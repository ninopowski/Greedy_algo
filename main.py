weights = {
    0: [22, 19],
    1: [10, 9],
    2: [9, 9],
    3: [7, 6]
}

different_weights = {
    0: [18, 21],
    1: [1, 2],
    2: [3, 1]
}

MAX_SPACE = 25


def greedy_alg(entry, space):
    total = 0
    ratios = {}
    for key, value in entry.items():
        ratios[key] = value[1] / value[0]
    sorted_weights = (sorted(ratios.items(), key=lambda x: x[1], reverse=True))
    while sorted_weights:
        index = sorted_weights[0][0]
        amount = entry[index][1]
        if total + amount < space:
            total += amount
            sorted_weights.pop(0)
        else:
            break
    print(f"The maximum non fractal weight that can be stored is: {total}")




greedy_alg(weights, MAX_SPACE)
greedy_alg(different_weights, MAX_SPACE)