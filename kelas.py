class Flight1:
    def __init__(self):
        return "Blank Constructor"
    def __init__(self,nama):
       self.nama = nama # self to assign set property
    def getName(self):# self utk akses  property constructor
        return self.nama
    def getRumah(self,rumah):
        self.rumah=rumah
        return self.rumah

class Flight:
    def number(self):
        return "12345"
    
t=Flight()
print(t.number())
t2=Flight1("yayan")
print(t2.getName())
print(t2.nama)
t2.nama="AraKiran"
print(t2.getName())
print(t2.getRumah("Saya"))
print(t2.rumah)
