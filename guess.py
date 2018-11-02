import random
r = random.randint(1, 100)
r1 = int( input('請猜數字1~100:'))

while (r1 < 1 or r1 > 100):
	r1 = int( input('請猜數字1~100:'))

while r1 != r:
	if r1 < r:
		print('比答案小')
	else:
		print ('比答案大')
	r1 = int(input('請猜數字1~100:'))

if r1==r:
	print('終於猜對了')