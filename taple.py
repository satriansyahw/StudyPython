t=("norway",1221.3,10)
p=("jepang",2,112.7)
print(t)
print(t[1])
hasil = t+p
print(hasil)
print(hasil[3])
tuple2d=(("a","b"),(1,2),(5,"B"))
print(tuple2d)
print(tuple2d[2])
print(tuple2d[2][0])
print(tuple2d[2][1])


tuple3d=(("a","b","c"),(1,2,"C"),(5,"B",1.2))
print(tuple3d)
print(tuple3d[2])
print(tuple3d[2][0])
print(tuple3d[2][1])
print(tuple3d[2][2])

def minmax(items):
    return min(items),max(items)

itemku =(10,2,33,100,4,23)
itemmu =[210,79,33,100,4,23]

print(minmax(itemku))
print(minmax(itemmu))
print(type(minmax(itemku)))
print(type(minmax(itemmu)))

a="Jelly"
b="bean"
a,b=b,a

print(a)
print(b)


