def exhaustive_search(current_sequence, remaining_parts, energy_so_far, best_sequence, min_energy):
    # Base case: if all parts are assembled
    if len(remaining_parts) == 0:
        if energy_so_far < min_energy:
            best_sequence = current_sequence.copy()
            min_energy = energy_so_far
        return best_sequence, min_energy

    # Recursive case: try assembling each remaining part in all possible orders
    for part in remaining_parts:
        next_sequence = current_sequence + [part]
        next_remaining_parts = [p for p in remaining_parts if p != part]

        # Calculate energy cost for assembling the next part
        energy_cost = calculate_cost(current_sequence[-1], part) if current_sequence else 0

        # Recursively explore the next assembly step
        best_sequence, min_energy = exhaustive_search(
            next_sequence,
            next_remaining_parts,
            energy_so_far + energy_cost,
            best_sequence,
            min_energy
        )

    return best_sequence, min_energy

def calculate_cost(current_part, next_part):
    # this part should be actual energy calculation
    return 1  

initial_sequence = []  # Start with an empty sequence
all_parts = [1, 2, 3, 4]  # Replace with the actual list of parts
best_sequence, min_energy = exhaustive_search([], all_parts, 0, [], float('inf'))

# Print the result
print("Best Sequence:", best_sequence)
print("Min Energy:", min_energy)
