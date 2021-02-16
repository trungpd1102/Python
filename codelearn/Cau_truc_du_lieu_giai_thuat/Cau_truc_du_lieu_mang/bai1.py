print("Nhập số n: ")
n = int(input())
a = []

for i in range(n):
    a.append(int(input()))
print("Nhập k:")
k = int(input())
print("Nhập x:")
x = int(input())

a.append(a[n-1])
print(a)
for i in range((n-1), k, -1):
    a[i] = a[i-1]
a[k] = x
print(a)

