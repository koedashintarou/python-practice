def gen0add():
	i= 1
	while i <= 30:
		yield i
		i += 2

it = gen0add()
for v in it:
	print(v, end=",")