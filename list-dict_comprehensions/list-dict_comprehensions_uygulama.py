import seaborn as sns

df=sns.load_dataset("car_crashes")
df.columns

#kolonları büyütme

df.columns=[columns.upper() for columns in df.columns]