X = int(input())

num_list = tuple(x**5 for x in range(10**4+1))
for i, a in enumerate(num_list):
    for j, b in enumerate(num_list):
        if a-b == X:
            print(i, j)
            exit(0)
        elif a+b == X:
            print(i, -j)
            exit(0)
