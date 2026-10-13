import numpy as np

#numpy vektörel işlemler için kullanılır hızlıdır ve kullanı basittir.Hızlı olmasının nedeni tek tipte değişken tutar tek tek değişkenlerin tipine vs bakmaz.
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
a*b

type(a)


#parantezin içine girilen boyut kadar 0 lardan oluşan liste oluşturma(parantezin içinde dtype ile tipi belirlenebilir)
np.zeros(5,dtype=int)

#numpy ile random sayı oluşturma
np.random.randint(0,10,size=5)

#ortalaması 10 standart sapması 4 olan 3 satır 4 sütun sayı listesi oluştur
np.random.normal(10,4,(3,4))


