num=int(input("Enter any number:"))
number=num
ans=0
while num >0:
    rem = num %10
    ans=ans*10 + rem
    num=num//10
if number==ans:
    print(ans," is palindrom")
else:
    print(ans,"is not palindrom")
