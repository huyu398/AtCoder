#!/usr/bin/env python3
import sys
from typing import List

import numpy as np

def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    MAX_SIZE = 1501
    plane = np.zeros((MAX_SIZE, MAX_SIZE), dtype=np.int64)
    for a, b, c, d in zip(A, B, C, D):
        plane[a, b] += 1
        plane[a, d] -= 1
        plane[c, b] -= 1
        plane[c, d] += 1

    cumulative_plane = plane.cumsum(axis=0).cumsum(axis=1)

    # 1 以上になっている要素の個数をカウントする
    print(np.count_nonzero(cumulative_plane >= 1))

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    C = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, A, B, C, D)

if __name__ == '__main__':
    main()
