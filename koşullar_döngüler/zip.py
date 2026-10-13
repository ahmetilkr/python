
students=["ahmet","ali","mehmet","davut"]
departments=["math","statistics","physics","astronomy"]
ages=[20,22,24,26]

#zip fonksiyonu verilen değişkenleri indexlere göre eşler
#list ise elemanları tek tek ayırarak listenin içine atar yani liste nesnesine dönüştürür
list(zip(students,departments,ages))

string="ahmet"
list(string)