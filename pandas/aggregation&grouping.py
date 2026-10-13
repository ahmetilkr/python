import pandas as pd
import seaborn as sns


pd.set_option("display.max_columns",None)

df=sns.load_dataset("titanic")
df.head()


#toplulaştırma(aggregation) bize özet istatistikler veren fonksiyonlardır bunlar:
# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

#groupby işleminden sonra aggregation fonksiyonları kullanılır


df.groupby("sex")["age"].mean()  #arka planda şöyle çalışır {"male":[0,1,2,3],"female":[4,5,6,7]}


df.groupby("sex").agg({"age":"mean"})        #üsttekiyle aynı ama bu kullanılmalı
df.groupby("sex").agg({"age":["mean","sum"]})            #sexe göre groupby yaptık buna cinsiyete göre kırmak denir


df.groupby("sex").agg({"age":["mean","sum"],
                       "embark_town":"count"})



df.groupby(["sex","embark_town"]).agg({"age":["mean","sum"],
                       "embark_town":"count"})



df.groupby(["sex","embark_town","class"]).agg({"age":"mean",
                                               "survived":"mean",
                                               "sex":"count"})
















