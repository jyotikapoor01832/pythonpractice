def computeHCF(num1, num2):
    """
    Computing HCF of two numbers
    """
    smaller =num2 if num1>num2 else num1   #concise way of writing if else statement
    hcf=1
    for i in range(1,smaller+1):
        if (num1%i ==0) and (num2%i == 0):
            hcf =i
    return hcf
num1 = 12
num2 = 16
print(f" H.C.F of {num1} and {num2} is ", computeHCF(num1,num2))  