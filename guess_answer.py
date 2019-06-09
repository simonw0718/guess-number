g_range_min = input('請輸入下限:')
g_range_max = input('請輸入上限:')
inputword = '請輸入數字介於'+ g_range_min+ '至' + g_range_max+ '之間:'
g_range_min = int(g_range_min)
g_range_max = int(g_range_max)

import random
answer = random.randint(g_range_min,g_range_max)

time = 1
while True:
	test = input(inputword)
	test = int(test)
	if test > answer:
		print('比答案大!')
		time += 1 # 快寫法time = time + 1
	elif test < answer:
		print('比答案小!')       
		time += 1
	else: 
		print('終於猜對了!', '你共猜了', time, '次', '答案是:',answer)
		break





