a = int(input())
b = int(input())
b_100 = b//100
b_10 = (b - 100*b_100) // 10
b_1 = b % 10
print(a * b_1)
print(a * b_10)
print(a * b_100)
print(a*b)