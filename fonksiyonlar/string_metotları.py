#dir(str) -->strinlerle kullanılacak metotları söyler
from pandas.util import capitalize_first_letter

name="ahmet"
name2="ahmet ilker kahraman"
name3="      ahmet      "
name4="ahmeta"
#len -->stringin kaç karakterden oluştuğunu gösteren fonksiyon
len(name)

#upper() --> tüm karakterleri büyük harflere dönüştürür
name.upper()

#lower() --> tüm karakterleri küçük harflere dönüştürür
name.lower()

#eğer bir fonksiyonsa direk type(fonksiyon_ismi) mesela type(len) ile tipini sorgularsın ama bir methotsa type(lower) yazarsan hata verir çünkü bu classa bağlı olan bir fonksiyon yani
#bir methottur o yüzden bunu type(str.lower) ile sorgulaman gerekli

#.replace("değiştirmek_istenen_karakter","neyle_değişeceği")
name.replace("a","e")

#.split() -->() parantezin içindeki karaktere bakarak stringi parantezin içinde bakarak o karakterden böler ve listeye aktarır
a=name2.split()
#type(a) -->liste döndürür

#.strip() -->kelimenin başındaki ve sonundaki harfleri kırpar neyi kırpacağını karar vermek için de () içine gireriz hiçbir şey girmezsen boşluğa göre kırpar
name3.strip()
name4.strip("a")

#.capitalize() --> ilk harfi büyütür
name.capitalize()
























