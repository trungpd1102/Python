print("Nhập số n: ")
n = int(input())
a = []

for i in range(n):
    a.append(int(input()))
print("Nhập k:")
k = int(input())

print("Nhập x:")
x = int(input())

result = a[:k] + [x] + a[k:]
print(result)
