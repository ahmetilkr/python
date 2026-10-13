import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)

pd.set_option("display.width",500)    #kod çıktısı yan yana olsun aşağı devam etmesin



df=sns.load_dataset("titanic")
df.head()



df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"] / 10).head()       #eğer direk head atmak istersek parantez () şart
(df["age2"] / 10).head()
(df["age3"] / 10).head()




#yukarıdakileri tek tek yapmak yerine
#apply fonksiyonu satrlarda ya da sütunlarda elimizdeki belirli bir fonksiyonu satırlara ve sütunlara uygular
df[["age","age2","age3"]].apply(lambda x:x/10).head()
df.loc[:, df.columns.str.contains("age")].apply(lambda x:x/10).head()


#değişiklikleri kaydetmek istersek
df.loc[:,["age","age2","age3"]]=df.loc[:, df.columns.str.contains("age")].apply(lambda x:x/10).head()
df.loc[:,df.columns.str.contains("age")]=df.loc[:, df.columns.str.contains("age")].apply(lambda x:x/10).head()

df.head()








