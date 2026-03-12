def number():
    for n in range(1, 11):
        yield n *n
for i in number():
    print(i)        