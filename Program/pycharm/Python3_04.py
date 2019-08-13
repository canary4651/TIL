def total(scores):
    total_score = 0
    for i in range(len(scores)):
        total_score += scores[i]
    return total_score

print(total([80,100,70,90,40]))

