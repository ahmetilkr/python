help()  #parantezin içine girilen fonksiyonun dokümantasyonun gösterir örnek verir argümanları vs

print("a", "b")  #bunun çıktısı a b şeklinde olur
print("a", "b", sep="__")  #bunun çıktısı a__b şeklinde olur

#""" """ fonksiyon içinde bu tırnakları koyup arasında entere basmanın işlevi fonksiyonu bilmeyen biri help(fonksiyon_ismi) yazınca bilgi sahibi olması bunun ismi docstring
def calculate(x):
    """
    sayının 2 ile çarpılmış halini veren fonksiyon
    Args:
        x: int,float   

    Returns:
        int,float
    """
    print(x * 2)


calculate(5)

def summer(arg1,arg2):
    print(arg1+arg2)

summer(5,7)


summer(arg2=8,arg1=7)  #bu şekilde de kullanılabilir



def divide(a,b=1):
    print(a / b)


divide(10)   #b argümanına değer girilmese bile ön tanımlı argüma yapıtğımız için (b=1) hata vermez
divide(10,2)   #b argümanına 2 verildiği için fonksiyonda parametre olarak tanımlanan (b=1) ezilir ve b 2 değerini alır



def calculate2(arg1,arg2):
    topla=arg1+arg2      #returnden sonra fonksiyonun kalan kısmı çalışmaz
    çıkar=arg1-arg2
    çarp=arg1*arg2
    üstünü_al=arg1**arg2

    return topla,çıkar,çarp,üstünü_al

topla,çıkar,çarp,üstünü_al=calculate2(4,5)     #sonuçlar tüm değişkenlere sırasıyla kaydedilir
cevaplar=calculate2(4,5)    #cevaplar değişkenine sonuç tuple olarak kaydedilir
















