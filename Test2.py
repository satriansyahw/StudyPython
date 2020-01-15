# string
name="kiran"
kar1=name[1]
print(kar1)
print(type(name))
print(name.capitalize())

anak=["Ara","Kiran"]
print('print pertama :' + anak[0])
print('print kedua : '+anak[1])

txt ="hai-hello-world"
txtsplit= txt.split('-')
print('Split 0 : '+txtsplit[0])
print('Split 1 : '+txtsplit[1])
print('Split 2 : '+txtsplit[2])

mylist=["apple","orange","grape",234,98.67]
mylist[2]=88

print(mylist[0])
print(mylist[2])
print(mylist[4])
print(mylist)
mylist.append("34")
print(mylist)

#Dictionary object

data ={"p1":"Yayan","p2":"Bintang","p3":"Ara","p4":"Kiran"}
print(data)
print(data['p3'])


myurl =  "sixty-north.com/c/t.txt"
from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words=[]
    for line in story:
        line_world=line.split()
        for world in line_world:
            story_words.append(world)
            
            print(story_words)
  


