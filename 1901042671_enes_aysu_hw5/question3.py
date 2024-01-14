def min_cost_alignment_with_operations(sequence1, sequence2, insertion_deletion_cost, substitution_cost):
    m, n = len(sequence1), len(sequence2)

    # initialize matrices
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    op = [[-1] * (n + 1) for _ in range(m + 1)]

    # initialize base cases
    for i in range(m + 1):
        dp[i][0] = i * insertion_deletion_cost
        op[i][0] = 2  # deletion
    for j in range(n + 1):
        dp[0][j] = j * insertion_deletion_cost
        op[0][j] = 1  # insertion

    # fill the matrices
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                op[i][j] = 0  #  match
            else:
                insertion_cost = dp[i][j - 1] + insertion_deletion_cost
                deletion_cost = dp[i - 1][j] + insertion_deletion_cost
                substitution_cost_total = dp[i - 1][j - 1] + substitution_cost

                if insertion_cost <= deletion_cost and insertion_cost <= substitution_cost_total:
                    dp[i][j] = insertion_cost
                    op[i][j] = 1  # insertion
                elif deletion_cost <= insertion_cost and deletion_cost <= substitution_cost_total:
                    dp[i][j] = deletion_cost
                    op[i][j] = 2  # deletion
                else:
                    dp[i][j] = substitution_cost_total
                    op[i][j] = 3  # substitution

    # backtracking to find the sequence of operations
    i, j = m, n
    operations_sequence = []
    while i > 0 or j > 0:
        if op[i][j] == 0:  # match
            operations_sequence.append("Match")
            i -= 1
            j -= 1
        elif op[i][j] == 1:  # insertion
            operations_sequence.append("Insertion")
            j -= 1
        elif op[i][j] == 2:  # deletion
            operations_sequence.append("Deletion")
            i -= 1
        else:  # substitution
            operations_sequence.append("Substitution")
            i -= 1
            j -= 1

    # reverse the operations sequence since we backtracked from the end
    operations_sequence.reverse()

    return dp[m][n], operations_sequence

# test usage
sequence1 = "AGTACGT"
sequence2 = "TCTAGCA"

insertion_deletion_cost = 1
substitution_cost = 3

min_cost, operations = min_cost_alignment_with_operations(sequence1, sequence2, insertion_deletion_cost, substitution_cost)
print(f"The minimum cost for aligning the sequences is: {min_cost}")
print(f"Sequence of operations: {operations}")
