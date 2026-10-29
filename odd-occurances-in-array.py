def solution(A):
    # Number of elements in the array
    n = len(A)

    # Sort so that equal values are next to each other
    A.sort()

    # Check A two elements at a time, e.g. (0,1), (2,3), ...
    # Stop at n - 1 so that A[i + 1] never uses a nonexistent index
    for i in range(0, n - 1, 2):

        # If the pair doesn't match, A[i] is the unpaired value
        if A[i] != A[i + 1]:
            return A[i]

    # If every pair matched, the unpaired value is the last element
    return A[-1]
