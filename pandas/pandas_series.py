import pandas as pd


#seriler tek boyutlu veri sütunudur.(numpydaki tek boyutlu dizilerin indexlenmiş hali)
s=pd.Series([10,77,12,4,5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)
