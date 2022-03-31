def update_score():
    score = 10
    nscore = 20
    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
            print(score)
        else:
            f.write(str(nscore))
            print(nscore)
update_score()