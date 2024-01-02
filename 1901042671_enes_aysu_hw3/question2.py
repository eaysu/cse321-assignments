def calculate_cost(assignment, cost_matrix):
    return sum(cost_matrix[user][processor] for user, processor in assignment)

def generate_permutations(n, current_permutation, permutations_list):
    if len(current_permutation) == n:
        permutations_list.append(current_permutation.copy())
        return

    for i in range(n):
        if i not in current_permutation:
            current_permutation.append(i)
            generate_permutations(n, current_permutation, permutations_list)
            current_permutation.pop()

def exhaustive_search(cost_matrix):
    n = len(cost_matrix)
    best_assignment = None
    min_cost = float('inf')

    permutations_list = []
    generate_permutations(n, [], permutations_list)

    for perm in permutations_list:
        assignment = list(enumerate(perm))
        total_cost = calculate_cost(assignment, cost_matrix)

        if total_cost < min_cost:
            min_cost = total_cost
            best_assignment = assignment

    return best_assignment, min_cost

# test
cost_matrix = [
    [2, 3, 1],
    [5, 4, 8],
    [7, 2, 6]
]

best_assignment, min_cost = exhaustive_search(cost_matrix)
print("Best Assignment:", best_assignment)
print("Minimum Cost:", min_cost)
