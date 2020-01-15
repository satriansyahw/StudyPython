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


class Terbang:
    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError("No airline code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid Route Number")
        self.numberku = number
        
    def number(self):
        return self.numberku
    
    def airline(self):
        return self.numberku[:2]


try:
    fly = Terbang("GA123")
    flyku = fly.numberku;
    print(flyku)
    print(fly.number())
except ValueError:
    print("Error, wrong flight ticket")
