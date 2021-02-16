print("nhap n")
n = int(input())
a = []


for i in range(1, (n+1)):
    a.append(i)
print(a)
print("nhap k")
k = int(input())

for i in range(k, (n-1)):
    a[i] = a[i + 1]

a.pop()

print(a)