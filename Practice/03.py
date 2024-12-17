def num2freq(a):
#     res = {}
#     for num in a:
#         if num in res:
#             res[num] += 1
#         else:
#             res[num] = 1
#     return res
    return {num: a.count(num) for num in a}

a = [1, 2, 3, 1, 2, 1, 4, 5, 2]
print(num2freq(a))
