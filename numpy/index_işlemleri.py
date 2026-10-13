import numpy as np

#aynı python listelerdeki gibi değiştirme işlemi yapılabilir
b=np.random.randint(10,size=10)
b[0]=99


#
a=np.random.randint(10,size=(3,5))
a[0,0]
a[1,1]
a[2,3]=999

a[0,0]=2.9   #numpy arrayi hızlı kılan tek tip değişken tutmasıdır bu yüzden float veri versem de bunu int olarak tuttu


a[:,0]        #tüm satırları 0. sütunu
a[1,:]        #1. satırı tüm sütunları
a[0:2,0:3]

