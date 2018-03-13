"""hw2_t1"""
print("enter integers X,Y,Z,N:")
X, Y, Z, N = (int(input()) for _ in range(4))
print([[a, b, c] for a in range(0, X+1)
       for b in range(0, Y+1)
       for c in range(0, Z+1)
       if sum([a, b, c]) != N])
