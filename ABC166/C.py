N, M = tuple(map(int, input().split()))
Hs = tuple(map(int, input().split()))

good = [True] * N

for _ in range(M):
    A, B = tuple(map(int, input().split()))
    H_A, H_B = Hs[A-1], Hs[B-1]
    if H_A < H_B:
        good[A-1] = False
    elif H_B < H_A:
        good[B-1] = False
    else:
        good[A-1] = good[B-1] = False

print(sum([v == True for v in good]))

# path = [[0] * N for _ in range(N)]
# for _ in range(M):
#     A, B = tuple(map(int, input().split()))
#     H_A, H_B = Hs[A-1], Hs[B-1]
#     path[A-1][B-1] = H_B
#     path[B-1][A-1] = H_A

# print(sum(all(Hs[i] > h for h in p) for i, p in enumerate(path)))
