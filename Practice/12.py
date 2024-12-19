# 数学: 80, 90, 70, 85, 95 ・英語: 70, 75, 80, 85, 90 ・国語: 75, 80, 85, 90, 95
score_math = [80, 90, 70, 85, 95]
score_english = [70, 75, 80, 85, 90]
score_japanese = [75, 80, 85, 90, 95]

average_math = sum(score_math) / len(score_math)
average_english = sum(score_english) / len(score_english)
average_japanese = sum(score_japanese) / len(score_japanese)

print(f"数学の平均点: {average_math:.2f}")
print(f"英語の平均点: {average_english:.2f}")
print(f"国語の平均点: {average_japanese:.2f}")
