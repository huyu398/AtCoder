A, B, N = [int(x) for x in input().split()]

# val = (int(A * i / B) - A * int(i / B) for i in range(1, N+1))
# print(max(val))

x = B - 1
if x > N:
    x = N
print(int(A * x / B) - A * int(x / B))
