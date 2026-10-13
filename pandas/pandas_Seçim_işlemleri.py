import pandas as pd
import seaborn as sns

from koşullar_döngüler.enumerate import index

df=sns.load_dataset("titanic")
df.head()
df.index

df[0:13]
df.drop(0,axis=0).head()  #drop silme işlemi yapar ilk parametre 0 ı sil axis=0 da satırlardan sil demek kalıcı olarak kaydedilmedi sadece gözlem

#eğer birden fazla satırı aynı anda silmek istersek kalıcı olarak kaydedilmedi sadece gözlem
delete_index=[1,3,5,7]
df.drop(delete_index,axis=0).head()

#kalıcı olarak kaydetmek için 2 yöntem var
df=df.drop(delete_index,axis=0)   #sildik ve yapılan değişikliği df değişkenine atadık artık kalıcı oldu
df.drop(delete_index,axis=0,inplace=True)   #inplace parametresi kalıcı olarak kaydeder


#değişkeni indexe çevirmek
df["age"].head()    #age değişkenini seçmek için kullanılır
df.age.head()       #age değişkenini seçmek için kullanılır bu şekilde de kullanılabilir yukarıdaki ile aynı şey

df.index=df["age"]  #bu işlemi  yaptıktan sonra df de sol tarafta index numaraları vardı 0 1 2 vs bunların yerine artık o kişilerin yaşları yer aldı
df.drop("age",axis=1).head()    #artık age sütununa ihtiyacımız yok silebilirz
df.drop("age",axis=1,inplace=True)   #kalıcı hale getirme



#indexi değişkene çevirmek

df["age"]=df.index  #eğer df["age] varsa o sütun seçilir yoksa o dataframe'e sütun eklemesi yapıalcak demektir
df.head()
df.drop("age",axis=1,inplace=True)


#indexi değişkene çevirmek 2.yol

df.reset_index()  #indexdeki değişkeni siler onu bir sütun olarak kaydeder 








