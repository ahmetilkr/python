import pandas as pd
import seaborn as sns


pd.set_option("display.max_columns",None)

df=sns.load_dataset("titanic")
df.head()


df[df["age"]>50].head()     #yaşı elliden büyük olanların 5 tanesi
df[df["age"]>50]["age"].count()        #yaşı elliden büyük olan kısmı döndürdükten sonra age sütununu seçip sayısını .count() ile öğreniyoruz


#tek koşulda bu şekilde
df.loc[df["age"]>50,["class","age"]].head()

#çift koşul varsa koşullar kesinlikle () alınmalı koşşular arasında & işareti var
df.loc[(df["age"]>50) & (df["sex"]=="male"),["class","age"]].head()


#daha fazla koşul
df_new=df.loc[(df["age"]>50)
       & (df["sex"]=="male")
       & (df["embark_town"]=="Southampton")|(df["embark_town"]=="Cherbourg"),["class","age","embark_town"]]

df_new["embark_town"].value_counts()
df_new["age"].value_counts()



















