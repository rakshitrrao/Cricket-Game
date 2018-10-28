import random





score=0
wickets=2
while True:
    b= input('enter number')
    f=int(b)
    v=random.randint(1,3)
    print(v)
    if f==v:
        print('out')
        wickets=wickets-1
        if wickets<=0:
            print('all out')
            break

    else:
        score=score+f
        continue



print('game over')
print('total score ',score)
