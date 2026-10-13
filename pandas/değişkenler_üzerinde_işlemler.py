import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)      #max kolon sayısı olmasın hepsini göster

df=sns.load_dataset("titanic")
df.head()

"age" in df
df["age"].head()
df.age.head()
type(df.age.head())   #pandas series

df[["age"]].head()
type(df[["age"]].head())  #pandas dataframe

df[["age","alive"]]  #birden fazla değişken seçmek için

col_name=["age","adult_male","alive"]
df[col_name]       #değişkenleri listeye atıp direk seçebiliriz

df["age2"]=df["age"]**2    #sütun ekleme
df["age3"]=df["age"]/df["age2"]     #sütun ekleme



df.drop("age3",axis=1).head()     #age3 sütunu sil
df.drop(col_name,axis=1).head()         #col_name listesi içindeki sütunları sil

df.loc[:,~df.columns.str.contains("age")].head()

type(df.columns)













