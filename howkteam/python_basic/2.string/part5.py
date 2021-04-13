a = 'Phạm Đức Trung'
print(a.split(' ', maxsplit=1))
print(a.split('c'))	# list trả lại k có 'c'
print(a.rsplit(maxsplit=1))

print(a.partition('c')) # tuple trả về có 'c'

print(a.startswith('P'))
print(a.endswith('un'))


print(a.find('ức')) # 6
print(a.find('úg')) # -1

print(a.index('ức')) # 6
print(a.find('úg')) # error

print(a.isupper())
print(a.islower())
print(a.istitle())
print(a.isdigit())
print(' '.isspace())




