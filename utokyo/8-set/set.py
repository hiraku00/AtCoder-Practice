def check_characters(str1):
    print(set(str1))
    print(len(set(str1)))
    return len(set(str1))
print(check_characters('Onde a terra acaba e o mar começa') == 13)

print(f'==================')

def check_dicsize(dic1):
    print(len(dic1))
    return len(dic1)
print(check_dicsize({'apple': 0, 'orange': 2, 'pen': 1}) == 3)

print(f'==================')

def count_words2(str_engsentences):
    str1 = str_engsentences.replace('.', '')
    # str1 = str1.lower()
    list1 = str1.split(' ')
    print(set(list1))
    print(len(set(list1)))
    return len(set(list1))
print(count_words2('From Stettin in the Baltic to Trieste in the Adriatic an iron curtain has descended across the Continent.') == 15)
