def _prime_number(_num):
	if _num < 2:
		return False

	elif _num == 2:
		return True
	elif _num == 3:
		return True

	else: 
		if _num % 2 == 0:
			return False
		else:	
			for i in range(3, (_num-1), 2):
				if _num % i == 0:
					return False
				else : return True

n = int(input())
a = []

for i in range(1,(n+1)):
    a.append(i)

b = []

for i in range(len(a)):
    if _prime_number(a[i]) is True:
        b.append(a[i])

print(b)
