def main():
    print("nhap n:")
    n = int(input())
    a = []

    print("nhap cac phan tu cua a:")
    for i in range(n):
        a.append(int(input()))
    print(a)

    if a[0] > a[1]:
        print(don_dieu_giam(n, a))
    elif a[0] < a[1]:
        print(don_dieu_tang(n, a))
    else: print("NO")


def don_dieu_tang(n, a):
    for i in range(1, (n-1)):
        if a[i] >= a[i+1]:
            return "NO"
    return "YES"


def don_dieu_giam(n, a):
    for i in range(1, (n-1)):
        if a[i] <= a[i+1]:
            return "NO"
    return "YES"    

if __name__ == "__main__":
    main()
