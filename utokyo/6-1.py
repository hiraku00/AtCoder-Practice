strings = ['The', 'quick', 'brown']
print([len(x) for x in strings])

str1 = '123,45,-3'
print([int(x) for x in str1.split(',')])

def var(lst):
    n = len(lst)
    av = sum(lst) / n
    return sum([(x - av)**2 for x in lst]) / n
print(var([3,4,1,2]) == 1.25)

def sum_lists(list1):
    return sum([sum(x) for x in list1])
print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)

def sum_matrix(list1, list2):
    return [[list1[i][j] + list2[i][j] for j in range(len(list2))] for i in range(len(list1))]
print(sum_matrix([[1,5,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]])==[[2, 9, 10], [6, 10, 14], [10, 14, 18]])
