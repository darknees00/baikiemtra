

def tinhtongSUM(n):
    tintong = 0
    while (n>0):
        tintong = tintong + n % 10
        n = int(n/10)
    return tintong
n = int(input("Nhập số nguyên dương n ="))
print("Tổng của các chữ số", n,"là", tinhtongSUM(n))