def max_score():
    with open('scores.txt', 'r') as f:
        score = f.readlines()
        print(score)
        print(type(score))
    return score
print(max_score())