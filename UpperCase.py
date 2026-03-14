list=["hello", "world"]
list2 = [ i.upper() for i in list]
print(list2)
list3 = [ i.lower() for i in list2]
print(list3)
for i in list2:
    print(i.upper())
    print(i.lower())
    
    
#Using Nested Loop to print[(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)] in a matrix format

list=[]
for i in range(3):
    for j in range(1,4):
        list.append((i,j))
        