
def int_to_roman(x):
	d = {
		1: 'I',
		4: 'IV',
		5: 'V',
		9: 'IX',
		10: 'X',
		40: 'XL',
		50: 'L',
		90: 'XC',
		100: 'C',
		400: 'CD',
		500: 'D',
		900: 'CM',
		1000: 'M'
	}
	if not isinstance(x, int):
		raise TypeError('На входе должно быть целое число')

	res = ""
	for i in sorted(d.keys(), reverse = True):
		n = x // i
		res += d[i] * n
		x -= n * i
		#print(x, i, res, n)

	return res


d1 = range(1,11)
d2 = [11] + list(range(20,110, 10))
d3 = list(range(200,1100,100)) + [1001]

for n1, n2, n3 in zip(d1, d2, d3):
	print(f'{n1:2} | {int_to_roman(n1):4} | {n2:3} | {int_to_roman(n2):4} | {n3:4} | {int_to_roman(n3):4}')