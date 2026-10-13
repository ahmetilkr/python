import numpy as np

v=np.array([1,2,3,4,5])

v/5
v*7
v**2

np.subtract(v,1)   #çıkarma
np.add(v,1)        #toplama
np.mean(v)         #ortlama
np.sum(v)          #tüm elemanlar toplamı
np.min(v)          #tüm elemanlar arasından en küçüğü
np.max(v)          #tüm elemanlar arasından en büyüğü
np.var(v)

#numpy ile iki bilinmeyenli denklem çözme
#5x0+x1=12
#x0+3x1=10

a=np.array([[5,1],[1,3]])
b=np.array([12,10])

np.linalg.solve(a,b)
