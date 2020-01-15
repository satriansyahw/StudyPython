x =list(range(5,10))
print(x)
for  xx in x:
    print(xx)
    
t=[6,45,224,534]
for p in enumerate(t):
    print(p)
    
ss ="show how to index into sequebces".split()
print(ss[1:3])
print(ss[0:1])

data = "belajar menggunakan bahasa python dan django".split()

print(data[1:3]) # >=1 & < 3
print(data[2:5])
print(data[2:4])

print(data.index('django'))
print(" ".join(data))
data.remove('django')
# print(data.index('django'))
print(" ".join(data))
data.insert(5,"flask")
hasil = " ".join(data)
print(hasil)
