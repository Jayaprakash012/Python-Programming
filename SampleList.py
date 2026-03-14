list1=[1,2,3,4,5]
list2=[ i for i in list1]
for i in list1:
    list2.append(i*2)
print(list2)    