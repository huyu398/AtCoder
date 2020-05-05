N, M = [int(x) for x in input().split()]

step = N // M
for i in range(1, N, step):
    print(i, i+1)
