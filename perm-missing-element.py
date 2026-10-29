def solution(A):
    # Number of elements in the array
    n = len(A)

    # Sort numbers from low to high
    A.sort()

    for i in range(n):

        # Index 0 should hold 1, index 1 should hold 2, and so on
        # The first index where A[i] != i + 1 shows which number is missing
        if A[i] != i + 1:

            # i + 1 is the number that should be here, so it is the missing one
            return i + 1

    # Every index matched, so the missing number is n + 1
    return n + 1
