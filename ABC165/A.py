K = int(input())
A, B = tuple(int(x) for x in input().split())

for i in range(A, B+1):
    if i % K == 0:
        print('OK')
        exit(0)

print('NG')

# start = (A // K) * K
# # if start % K == 0:
# #     import ipdb; ipdb.set_trace()
# #     print('OK')
# #     exit(0)

# if start == B or start + K <= B:
#     print('OK')
#     exit(0)

# print('NG')
