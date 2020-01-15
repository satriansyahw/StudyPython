import datetime
print(str(datetime.datetime.now()))

# error konversi: strongly type dynamic
def add(a,b):
    return a+b
print(add(9.5,int("5")))
print(add(4.5,"5"))
