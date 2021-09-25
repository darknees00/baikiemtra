def tinhgiaithua(n):
    if(n<0):
        int(input("Nhập lại số nguyên dương:"))
    if (n == 0 or n == 1):
       return 1
    return n* tinhgiaithua(n-1)
n = int(input("Nhập số nguyên dương n = "));
print("Giai thừa của", n, "là", tinhgiaithua(n));