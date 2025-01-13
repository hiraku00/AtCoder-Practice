ls = [3,-8,1,0,7,-5]

print(f'=========================== max')
print(max(ls))
print(max(ls, key=abs))
print(f'=========================== sorted')
print(sorted(ls))
print(sorted(ls, key=abs))
print(sorted(ls, reverse=True))
def invert(x):
    return -x
print(sorted(ls, key=invert))
print(sorted(ls, reverse=False))
print(f'=========================== lambda')
print(sorted(ls, key=lambda x: -x))
print(f'=========================== map')
print([abs(x) for x in [3,-8,1,0,7,-5]])
print([x for x in map(abs, [3,-8,1,0,7,-5])])
print(list(map(abs, [3,-8,1,0,7,-5])))
print(f'=========================== filter')
def pos(x):
    if x>0:
        return True
    else:
        return False
print(list(filter(pos, [3,-8,1,0,7,-5])))
print([x for x in [3,-8,1,0,7,-5] if pos(x)])

print(f'=========================== Practice 1')
def max_value_key(d):
    return max(d, key=lambda x: d[x])

print(max_value_key({3:10, 5:2, 9:1}) == 3)

print(f'=========================== Practice 2')
def max_abs(ln):
    return max(map(abs, ln))

print(max_abs([3,-8,1,0,7,-5]) == 8)

print(f'=========================== Practice 3')
def number_of_big_numbers(ln, n):
    return len(list(filter(lambda x: x > n, ln)))

print(number_of_big_numbers([10, 0, 7, 1, 5, 2, 9], 5) == 3)

print(f'=========================== Practice 4')
def number_of_long_lines(file, n):
    with open(file, 'r', encoding='utf-8') as f:
        return len(list(filter(lambda x: len(x) > n, f)))

print(number_of_long_lines('jugemu.txt', 10) == 6)
