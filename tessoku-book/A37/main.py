#!/usr/bin/env python3
import sys


def solve(N: int, M: int, B: int, A: "List[int]", C: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, B, A, C)

if __name__ == '__main__':
    main()
