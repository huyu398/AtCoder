N = int(input())
As = tuple(map(int, input().split()))

cnt = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if j - i == As[i] + As[j]:
#             cnt += 1

for i, a in enumerate(As):
    end = i+a if i+a <= N else N
    forward = As[end+1:]

    hoge = list(j+1 == v for j, v in enumerate(forward))

    cnt += sum(hoge)

    # end = i-a if i-a >= 0 else 0
    # backward = As[:end+1]
    
    # import ipdb; ipdb.set_trace()

print(cnt)
