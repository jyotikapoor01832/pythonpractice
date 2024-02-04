a, b = 0, 1
length=int(input("Enter a length of series: "))
print(a)
print(b)
for i in range(length):
    c = a + b
    print(c)
    a = b
    b = c