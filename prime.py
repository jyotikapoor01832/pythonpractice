num=int(input("Enter any number:"))
if num==1:
    print(num,"is not prime number")
elif num>1:
    for i in range (2,num):
        if num%i==0:
            print(num,"is not prime")
            break
    else:
        print(num, "is prime")
else:
    print(num,"is not prime")