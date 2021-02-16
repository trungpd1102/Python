print("nhap n:")
n = int(input())
a = []

print("nhap cac phan tu cua a:")
for i in range(n):
    a.append(int(input()))
print(a)

kt_tang = True
kt_giam = False

for i in range (1, n):
    if