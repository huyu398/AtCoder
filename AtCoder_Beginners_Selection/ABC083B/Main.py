N, A, B = tuple(int(x) for x in input().split())

def sum_of_digits(value):
    return sum(int(d) for d in str(value))

retv = sum(v for v in range(1, N+1) if A <= sum_of_digits(v) <= B)
print(retv)
