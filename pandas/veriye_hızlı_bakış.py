import pandas as pd
import seaborn as sns


#read_format methodu bilgisayarındaki dosyaları okumak için koullanılır load_dataset ise dışarıdaki bir veri setini indirmek için kullanılır
#titanic seaborn kütüphanesinde hazır şekilde bulunan bir veri seti
df=sns.load_dataset("titanic")
df.head()
df.tail()
df.info()      #daha detaylı bilgi verir heade göre
df.shape
df.columns
df.index
df.describe().T    #hızlı özet bilgiler transpoz alma amacı okunabilirliği arttırmak
df.isnull().values.any()   #df.isnull() yaparsan boş olanlara true olmayan değerlere false verir .values yaparsan bunun değerlerni numpy arrayının içine atar .any() 1 tane bile true varsa true döner
df.isnull().sum()   #her bir değişkende kaç tane eksik değer var onu hesaplar isnull() önce sütun isimleri durarak değerleri true false yapar sum alt alta toplayarak değerleri söyler
df["sex"].head()
df["sex"].value_counts()   #bir kategorik değişkenin(sayılarla değil gruplarla vs tutulan str) içindeki gruplartan kaçar tane var

