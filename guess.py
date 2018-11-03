import random
r = random.randint(1, 100)
r1 = input('請猜數字 1 ~ 100: ')
while True:
	if str.isnumeric(r1) == False:
		r1 = input('輸入錯誤！ 請猜 “數字” 1 ~ 100: ')
	else:
		if (int(r1) < 1 or int(r1) > 100):
			r1 = input('輸入錯誤！ 請猜 數字 ”1 ~ 100": ')
		elif int(r1) != r:
			if int(r1) < r:
				r1 = input('比答案小, 再猜猜看:')
			else:
				r1 = input('比答案大, 再猜猜看:')
		else: 
			print('終於猜對了！')
			break

