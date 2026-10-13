import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)

pd.set_option("display.width",500)    #kod çıktısı yan yana olsun aşağı devam etmesin



df=sns.load_dataset("titanic")
df.head()


#2. parametre satırlarda hangi değişken yer alacak 3. değişken sütunlarda hangi değişken yer alacak ilk parametre ise bu sütun ve satırların kesişiminde hangi değişken yer alacaki
#pivot tableın default fonksiyonu mean() dir o yüzden başka bir fonksiyon vermezsen oto ortalama alır
df.pivot_table("survived","sex","embarked")



#default fonksiyonunu değiştirmek istersek:
df.pivot_table("survived","sex","embarked",aggfunc="std")


#sütunda hem embarked hem class olur 2. boyut eklenmiş olur
df.pivot_table("survived","sex",["embarked","class"])


#hem satır hem sütun iki seviyeli
df.pivot_table("survived",["sex","adult_male"],["embarked","class"])


#qcut ve cut elindeki sayısal değişkeni kategorik değişkene çevirir
df["new_age"] = pd.cut(df["age"],[0,10,18,25,40,90])
df.pivot_table("survived","sex","new_age")



df.pivot_table("survived","sex",["new_age","class"])
