import numpy as np
import pandas as pd

m=np.random.randint(1,30,(5,3))
df1=pd.DataFrame(m,columns=["var1","var2","var3"])    #dataframe sıfırdan dataframe oluşturur
df2=df1+99


pd.concat([df1,df2])      #iki tane df birleştirme


pd.concat([df1,df2],ignore_index=True)     #yukarıdakinde index iki tabloyu birleştirdiğimiz için 0 1 2 3 4 0 1 2 3 4 şeklindeydi ignore_index bunu düzeltir


#merge ile birleştirme işlemleri
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})


pd.merge(df1,df2,on="employees")   #iki df birleştirir on parametresi hangi değişkene göre birleştirme yapılacak onu söyler


df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)

