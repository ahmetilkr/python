
dictionary = {"isim":"ahmet",
            "yaş":21,
            "şehir":"balıkesir"}

dictionary2 = {"isim":["ahmet","ilker"],
            "yaş":21,
            "şehir":"balıkesir"}

dictionary["isim"]
dictionary2["isim"][1]


"isim" in dictionary #sözlüğün içinde key var mı yok mu diye sorgulamak için

dictionary2.get("isim")  #keye göre valueye erişmek için

dictionary["isim"]="artık ahmet değil"  #keyin valuesini değiştirme

dictionary.keys()  #sözlüğün keylerine erişmek için

dictionary.values() #sözlüğün valuelerine erişmek için

dictionary.items()  #key ve karşılık gelen valueleri tuple olarak döndürür

dictionary.update({"isim":"ilker"}) #güncelleme yapmak için

dictionary.update({"isim_var_mı":"ilker"}) #eğer key bulunamazsa yeni değer olarak atanır




