A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
print("Danh sách A:", A)
print("Danh sách B:", B)
C = list(set(A) & set(B))

print("Các phần tử trùng nhau trong 2 mảng là:", C)

D = list(set(A) ^ set(C))
print("Các phần tử không trùng nhau ở list A là:", D)

E = list(set(B) ^ set(C))
print("Các phần tử không trùng nhau ở list B là:", E)