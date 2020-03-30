N = int(input())
a_list = list(int(a) for a in input().split())

def a_generator(a_list):
    cnt = 0
    while a_list:
        yield a_list.pop(a_list.index(max(a_list)))
        cnt += 1

    if cnt % 2:
        yield 0

alice, bob = [], []
a_iter = a_generator(a_list)

for a_v, b_v in zip(a_iter, a_iter):
    alice.append(a_v)
    bob.append(b_v)

print(sum(alice) - sum(bob))
