K, N = tuple(int(v) for v in input().split())

A_list = list(int(a) for a in input().split())

# # 各点の距離
# x_iter = iter(A_list)
# y_iter = iter(A_list)
# next(y_iter)
# 
# d_list = [y - x for x, y in zip(x_iter, y_iter)]
# d_list.append(K - A_list[-1] + A_list[0])
# d_list += d_list
# 
# l = len(d_list) // 2
# # sum_d = [sum(d_list[i:i+l-1]) for i in range(l)]
# min_d = min(sum(d_list[i:i+l-1]) for i in range(l))
# 
# print(min_d)

A_list += [a + K for a in A_list[:-1]]
print(min(A_list[i+N-1] - A_list[i] for i in range(N)))
