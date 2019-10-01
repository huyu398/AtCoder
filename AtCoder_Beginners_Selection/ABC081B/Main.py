def check_operatable(a_list):
    for a in a_list:
        if a % 2:
            return False
    return True

n = int(input())
a_list = list(map(int, input().split()))
cnt = 0
while check_operatable(a_list):
    a_list = [a // 2 for a in a_list]
    cnt += 1
print(cnt)
