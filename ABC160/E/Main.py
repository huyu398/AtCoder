X, Y, A, B, C = tuple(int(v) for v in input().split())
p_list = sorted((int(v) for v in input().split()), reverse=True)
q_list = sorted((int(v) for v in input().split()), reverse=True)
r_list = sorted((int(v) for v in input().split()), reverse=True)

p_list = p_list[:X]
q_list = q_list[:Y]
all_apple = sorted(p_list + q_list + r_list, reverse=True)

yummy = sum(all_apple[:X+Y])
# # 赤リンゴを食べる
# for _ in range(X):
#     if p_list[-1] >= r_list[-1]:
#         yummy += p_list.pop()
#         if len(p_list) == 0:
#             p_list = [0]
#     else:
#         yummy += r_list.pop()
#         if len(r_list) == 0:
#             r_list = [0]
# # 緑リンゴを食べる
# for _ in range(Y):
#     if q_list[-1] >= r_list[-1]:
#         yummy += q_list.pop()
#         if len(q_list) == 0:
#             q_list = [0]
#     else:
#         yummy += r_list.pop()
#         if len(r_list) == 0:
#             r_list = [0]

print(yummy)
