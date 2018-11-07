mulfunc = lambda x,y : x*y
filfunc = lambda x:  (x%4 == 0)
l1 = [1,2,3]
l2 = [10,20,30,40]

print(mulfunc(3,2))
print(list(map(mulfunc, l1,l2)))
print(list(filter(filfunc, l2)))
