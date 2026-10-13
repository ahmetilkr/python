liste=["ahmet",17,"liste",10.2,True,[1,2,3]]
liste2=[1,2,3,4,1,5,6,1]
liste[0]
liste[5][2]
liste[0]="değişti"
liste[0:4]

#.append("555") -->listenin sonuna ekleme yapar
liste.append("555")

#.pop() --> indexe göre eleman siler ve silinen elemanı döndürür bir değişkene atanıp kullanılabilir
liste.pop(6)

#.insert() --> indexe göre eleman ekler
liste.insert(2,"ekleme")

#.count() --> parantezin içine girilen eleman o listede kaç kere tekrar ediyor
liste2.count(1)

#.copy() -->listenin kopyasını oluşturur
yeni_liste=liste.copy()

#.remove() --> parantezin içine girilen elemanı siler (ilk bulduğu anda bütün hepsini değil)
liste2.remove(1)

#.reverse() -->listeyi tersine çevirir
liste.reverse()

#.sort() -->listeyi büyükten küçüğe veya alfatik olarak A-Z ye sıralar
liste.sort()

#.clear() -->listeyi tamamen boşaltır
liste.clear()









