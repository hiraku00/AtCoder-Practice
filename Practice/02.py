a = {"apple": 5, "banana": 2, "cherry": 8}
sorted_key = dict(sorted(a.items(), key=lambda x: x[1]))
print(sorted_key)
