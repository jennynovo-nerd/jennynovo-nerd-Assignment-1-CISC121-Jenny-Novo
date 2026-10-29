def solution(A):
    # Length of the array
    n = len(A)

    # Sort numbers from low to high
    A.sort()

    for i in range(n):

        # Index 0 should hold 1, index 1 should hold 2, and so on
        # The first index where A[i] != i + 1 means it is not a permutation.
        if A[i] != i + 1:

            # A number is missing, repeated, or not between 1 and n
            return 0

    # Every index matched, so A contains every number from 1 to n exactly once
    return 1
