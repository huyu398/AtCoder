#!/usr/bin/env python3
import sys
from typing import List
import itertools

def solve(N: int, K: int, A: "List[int]"):
    # A の累積和を求める
    accumulative_A = (0,) + tuple(itertools.accumulate(A))
    # 尺取法で累積和の差分が K 以下となる組み合わせの数を求める
    ans = 0
    idx = 0
    for i, a1 in enumerate(accumulative_A[:-1]):
        # K 以下となる要素が見つかるまで idx を大きくする
        while idx < N+1 and accumulative_A[idx] - a1 <= K:
            idx += 1
        ans += idx - i - 1
        # print(i, idx, idx - i - 1)

    print(ans)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
