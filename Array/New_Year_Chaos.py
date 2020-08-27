def minimumBribes(Q):
    moves = 0 
    # Q = [P-1 for P in Q]

    for i,P in enumerate(Q):
        # print(i,P - i - 1)
        if P - i - 1 > 2:
            print("Too chaotic")
            return

        for j in range(max(P-2,0),i):
            if Q[j] > P:
                moves += 1
    print(moves)