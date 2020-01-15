stocks={"A":100,"B":300,"C":1204}
print(stocks)
stocks.update({"C":500})
print(stocks)

buah1={"Apple","Durian","Orange","Anggur"}
buah2 ={"Durian","Jeruk"}
buah = buah1.union(buah2)
buahall = list(buah1)+list(buah2)
buahintersec = buah1.intersection(buah2)
buahdiff= buah1.difference(buah2)
print(buah)
print(buahall)
print(buahintersec)
print(buahdiff)