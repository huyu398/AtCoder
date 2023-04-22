#!/usr/bin/env python3
import sys

def query(n: int):
    print(f'? {n}')

def main():
    N = int(input())
    left = 0
    right = N
    mid = (left + right) // 2
    while right - left > 1:
        query(mid)
        ans = int(input())
        if ans == 0:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2

    print(f'! {mid}')

if __name__ == '__main__':
    main()
