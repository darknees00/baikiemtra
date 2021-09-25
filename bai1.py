
A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
B = []
lena = len(A)
for i in range(0, lena-1):
    if(A[i]<30):
        B.append(A[i])
print(B)


A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
B = []
lenA=len(A)
n= int(input("nhập số:"))
for x in range(0, lenA-1):
    for y in range(x, lenA):
        if(A[x]>A[y]):
            temp=A[y]
            A[y]=A[x]
            A[x]=temp
for z in range(0, lenA):
    if(A[z]>n):
        B.append(A[z])
print(B)
