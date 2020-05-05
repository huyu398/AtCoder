N, K = tuple(map(int, input().split()))

treat = [False] * N

for _ in range(K):
    d = int(input())
    for i in map(int, input().split()):
        treat[i - 1] = True

print(sum([v == False for v in treat]))
