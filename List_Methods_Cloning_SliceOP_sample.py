l=[]
print(l)
l1=l[:] #[start:end:step]
print(l1)
l1.extend(range(11))
print(l)
print(l1)
print(id(l))
print(id(l1))
