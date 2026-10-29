def solution(X, Y, D):
    # the distance the frog needs to travel
    distance = Y - X

    # number of full jumps
    jumps = distance // D

    # another jump is needed to get to the end if there is still some distance left
    if distance % D != 0:
        jumps += 1

    return jumps
