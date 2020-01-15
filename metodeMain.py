def luas_segitiga(alas,tinggi):
    hasil = 0.5 * alas* tinggi
    return hasil
def luas_persegi(panjang,lebar):
    hasil= panjang * lebar
    print("hasilnya:{}",format(hasil))
#similar to out ref C#
def modifyByRef(k):
    k.append(77)
    print ("nilai K = ",k)
def metodeWithDefaultValueparameter(message,border=' - '):
    line=border*len(message)
    print(line)
    print(message)
    print(line)
    
def main():
    luassegitiga = luas_segitiga(5,8)
    luas_persegi(10,5)
    print(luassegitiga)
    a=10
    b=a
    print(str(a==b))
    m=[12,16,18]
    modifyByRef(m) 
    print(m)
    metodeWithDefaultValueparameter("Hello python")
    metodeWithDefaultValueparameter("Hello python","*")
    


   
    
    
    

       
if __name__=="__main__":
    main()