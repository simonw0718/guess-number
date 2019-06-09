g_range_min = input('請輸入下限:')
g_range_max = input('請輸入上限:')
inputword = '請輸入數字介於'+ g_range_min+ '至' + g_range_max+ '之間:'
g_range_min = int(g_range_min)
g_range_max = int(g_range_max)

import random
answer = random.randint(g_range_min,g_range_max)
test = input(inputword)
test = int(test)
time = 1
while test != answer:	
    if test > answer:
        print('比答案大!')
        test = input(inputword)
        test = int(test)
        time = time + 1
    elif test < answer:
        print('比答案小!')
        test = input(inputword)
        test = int(test)
        time = time + 1
print('終於猜對了!', '你共猜了', time, '次', '答案是:',answer)





