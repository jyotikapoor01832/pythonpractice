def newList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(f"Multiplied numbers in list 1 : ",newList(list1))
print("Multiplied numbers in list 2 : ",newList(list2))