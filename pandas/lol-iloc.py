import pandas as pd
import seaborn as sns


pd.set_option("display.max_columns",None)

df=sns.load_dataset("titanic")
df.head()

#iloc indexe göre seçim yapar lox labellera göre seçim yaapr

#iloc:integer based selection
df.iloc[0:3]    #alışık olduğumuz gibi seçim 0 1 2. satırlar
df.iloc[0,0]


#loc:label based selection
df.loc[0:3]   #normalden farkı burada 3 dahil

df.loc[0:3,"age"]      #[satır,sütun]

col_names=["age","embarked","alive"]
df.loc[0:3,col_names]


df.iloc[0:3,0:3]
