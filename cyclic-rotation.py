def solution(A, K):
    # Number of elements in the array
    n = len(A)

    # An empty array has nothing to rotate, so return it
    # This also prevents a divide-by-zero error in K % n below
    if n == 0:
        return A

    # Rotating n times returns the array to its original order, so k rotations are equivalent to (K mod n) rotations
    k = K % n

    # No rotation needed, so return a copy of the array
    if k == 0:
        return A[:]

    # Rotating right k times moves the last k elements to the front
    # A[-k:] = last k elements, A[:-k] = everything before them
    return A[-k:] + A[:-k]
