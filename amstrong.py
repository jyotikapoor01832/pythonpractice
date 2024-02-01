num=int(input("Enter any number:"))
sum=0
number=num
while number>0:
    rem=number%10
    sum=sum+rem**3
    number=number//10
if num==sum:
    print(num,"is an Amstrong number")
else:
    print(num,"is not an Amstrong number")