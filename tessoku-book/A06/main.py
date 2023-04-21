#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, A: "List[int]", L: "List[int]", R: "List[int]"):
    # 引き算しやすいように 0 日目から配列を作る
    cumulative_A = [0]
    for i, a in enumerate(A):
        cumulative_A.append(cumulative_A[i] + a)

    for l, r in zip(L, R):
        print(cumulative_A[r] - cumulative_A[l-1])

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, Q, A, L, R)

if __name__ == '__main__':
    main()
