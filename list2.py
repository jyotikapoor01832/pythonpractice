lst = [10,20,30,40,50]
product = 1
index = 0
print("List is : ",lst)

while index < len(lst):
    product = product * lst[index]
    index +=1
print("Product of all numbers in a list is : ",product)