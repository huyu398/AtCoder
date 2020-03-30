N, Y = tuple(int(x) for x in input().split())

# 桁数が多くなるので，下 3 桁の 0 を消す
#   10000 -> 10, 5000 -> 5, 1000 -> 1
Y //= int(1e3)

def check_otoshidama(N, Y):
    # （ほぼ）全探索
    # NOTE: TLE した
    for i in range(N+1):
        # 枝切り
        #   5 * (N-i) が以降のループで出せる最大値
        #   Y - 10 * i が最大値より大きいならループする意味無し
        if Y - 10 * i > 5 * (N - i):
            continue

        for j in range(N+1):
            # 枝切り
            #   (N-i-j) が以降のループで出せる最大値
            #   Y - 10 * i - 5 * j が最大値より大きいならループする意味無し
            if Y - 10 * i - 5 * j > (N - i -j):
                continue

            for k in range(N+1):
                otoshidama = 10 * i + 5 * j + k
                if otoshidama == Y and i + j + k == N:
                    return i, j, k

    return -1, -1, -1

def explore_otoshidama(N, Y):
    # お札の枚数が一番少なくなる組み合わせ（N を考えない）
    I = Y // 10
    J = (Y - 10 * I) // 5
    K = (Y - 10 * I - 5 * J)
    # 1000 円が最小単位なので，1000 円札の枚数は K + 5n になるはず

    # I,J,K の合計が N より大きいなら求まる組み合わせはない
    if I + J + K > N:
        return -1, -1, -1
    # I,J,K の合計が N と一致するなら最小枚数が解
    if I + J + K == N:
        return I, J, K

    # 探索する
    for i in reversed(range(I+1)):
        # 仮に残りのお札が全部 5000 円とする
        J = N - i - K
        for k, j in enumerate(reversed(range(J+1))):
            # 一致するなら終了
            if 10 * i + 5 * j + K + k == Y:
                return i, j, K + k

    return -1, -1, -1

print(*explore_otoshidama(N, Y))
