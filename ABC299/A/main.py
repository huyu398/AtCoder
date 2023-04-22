#!/usr/bin/env python3
import sys

YES = 'in'
NO = 'out'

def solve(N: int, S: str):
    start = S.find('|')
    end = S.rfind('|')
    target = S.find('*')
    print(YES if start <= target <= end else NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
