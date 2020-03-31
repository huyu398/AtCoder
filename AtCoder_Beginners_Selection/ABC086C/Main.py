N = int(input())

def can_deer_move(t, start, end):
    # start から end に直角に移動したとき，時刻がどれくらいかかるか
    #   ETA = estimated time of arrival
    eta = sum(abs(s - e) for s, e in zip(start, end))

    # 時刻 t 以内に到着できない
    if eta > t: return False

    # 終点で反復移動を繰り返して，時刻を経過させる
    # 偶数なら終点に戻れるが，奇数なら終点に戻れない
    return not (t - eta) % 2

t0 = 0
position = (0, 0)

for _ in range(N):
    t, x, y = tuple(int(v) for v in input().split())

    if can_deer_move(t - t0, position, (x, y)):
        t0 = t
        position = (x, y)
    else:
        print('No')
        break
else:
    print('Yes')
