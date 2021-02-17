# "*" là import mọi thứ trong thư viện
from decimal import * 

# Lấy tối đa 30 số phần nguyên và phần thập phân
getcontext().prec = 30
a = Decimal(10) /3

print(a)
print(type(a))