def jaccard(a, b):
    return len(a & b) / len(a | b)

A = {"apple", "banana", "cherry"}
B = {"apple", "cherry", "orange"}
print(f"A & B : {len(A & B)}: {A & B}")
print(f"A | B : {len(A | B)}: {A | B}")
print(f"Jaccard係数 = |A ∩ B| / |A ∪ B| = {len(A & B)} / {len(A | B)} = {jaccard(A, B)}")
