def update_score(score, nscore):
    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            a = score
            f.write(str(a))
        else:
            a = nscore
            f.write(str(a))
        print(a)

update_score(10,20) #path1
update_score(30,10) #path2
