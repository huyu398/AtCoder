#!/usr/bin/env python3
import sys


def solve(T: int, N: int, L: "List[int]", R: "List[int]"):
    staff_diffs = [0] * (T+1)
    for l, r in zip(L, R):
        staff_diffs[l] += 1
        staff_diffs[r] -= 1

    hour_staffs = [0]
    for i, diff in enumerate(staff_diffs):
        hour_staffs.append(hour_staffs[i] + diff)
    hour_staffs.pop(0)
    hour_staffs.pop()

    for staff in hour_staffs:
        print(staff)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(T, N, L, R)

if __name__ == '__main__':
    main()
