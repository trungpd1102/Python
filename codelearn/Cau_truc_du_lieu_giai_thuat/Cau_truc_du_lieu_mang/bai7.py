print('Nhập n')
n = int(input())
a = []
b = []

print('Nhập các phần tử của a')
for i in range(n):
    a.append(int(input()))
a.sort() #Sắp xếp list a tăng dần

for i in range(n):
    count = 0
    for j in range(n):
        if a[j] == a[i]:
            count += 1
    if [a[i], count] not in b:
        b.append([a[i], count])

_result = ""
for i in range(len(b)):
    _result += str(b[i][0]) +" " + "-" +" " + str(b[i][1]) + ";" + " "

print(_result)