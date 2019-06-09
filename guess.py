import random
answer = random.randint(1,10)
test = input('請輸入1~10數字:')
test = int(test)
while test != answer:
    if test > answer:
        print('比答案大!')
        test = input('請輸入1~10數字:')
        test = int(test)
    elif test < answer:
        print('比答案小!')
        test = input('請輸入1~10數字:')
        test = int(test)
print('終於猜對了!答案是:',answer)





