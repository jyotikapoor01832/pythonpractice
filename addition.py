num=int(input("Enter any number:"))
if num<0:
    print("Enter positive number.")
else:
    sum=0
    while(num>0):
        sum=sum+num
        num=num-1
    print("Sum is:",sum)
