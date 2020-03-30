N = int(input())
d_list = list(int(input()) for _ in range(N))

def d_generator(d_list):
    while len(d_list):
        mochi = max(d_list)
        yield mochi
        d_list = tuple(d for d in d_list if d is not mochi)

print(len(tuple(d_generator(d_list))))
