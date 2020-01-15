def luas_segitiga(alas,tinggi):
    hasil = 0.5 * alas* tinggi
    return hasil
def luas_persegi(panjang,lebar):
    hasil= panjang * lebar
    print("hasilnya:{}",format(hasil))
def main():
    luassegitiga = luas_segitiga(5,8)
    luas_persegi(10,5)
    print(luassegitiga)

if __name__=="__main__":
    main()