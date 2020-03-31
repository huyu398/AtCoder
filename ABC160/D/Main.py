N, X, Y = tuple(int(v) for v in input().split())

ans = [0 for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        # 単純な距離
        d = j - i

        # 短絡パスを使った距離
        #   始点から X まで行く
        to_X   = abs(X-1 - i)
        #   Y から終点まで行く
        from_Y = abs(Y-1 - j)
        d_p = to_X + from_Y + 1
        ans[min(d, d_p)] += 1
        # if i <= X-1 and Y-1 <= j:
        #     d -= Y - X - 1
        # print(i+1, j+1, d)
        # ans[d] += 1

for n in ans[1:]:
    print(n)
