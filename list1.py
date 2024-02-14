l1=[12,23,34,45,56,67,78,89]
print("Given list is ",l1)
print("First element in given list is ",l1[0])
print("Second element is ",l1[1])
print("Last element is ",l1[-1])
print ("Second element to fifth element ",l1[2:6])

#add element in the list
l1.append(11)
print("After adding element using append method", l1)

#add element at any position in a list
l1.insert(1,21)
print("After adding vlaue using insert method", l1)

#change list item
l1[1]=22
print("After changing value of second item to 22 list becomes",l1)

#remove item from list
l1.remove(22)
print("List becomes",l1)

#length of list
print("Length of given list is",len(l1))

#list in loop
for i in l1:
    print(i)

#list comprehension
x=[x for x in l1]
print("using list comprehension list :",x)

y=[y for y in l1 if y>50]
print("List become",y)

#sorting in ascending  of list
l1.sort()
print("List after sorting",l1)
#sorting in descending of list
l1.sort(reverse=True)
print("Sorting in descending order",l1)

#clear list
l1.clear()
print("After clearing list becomes:",l1)