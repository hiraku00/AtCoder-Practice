def word2freq(b):
    # res = {}
    # for word in b:
    #     if word in res:
    #         res[word] += 1
    #     else:
    #         res[word] = 1
    # return res
    return {word: b.count(word) for word in b}

b = ["apple", "banana", "apple", "cherry", "cherry", "cherry", "banana", "apple", "apple", "cherry"]
print(word2freq(b))
