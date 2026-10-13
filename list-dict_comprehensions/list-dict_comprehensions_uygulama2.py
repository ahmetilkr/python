import seaborn as sns

df=sns.load_dataset("car_crashes")
df.columns

#kolonları büyütme

df.columns=[columns.upper() for columns in df.columns]

#isminde INS olanların başına FLAG olmayaanların NO_FLAG eklemek istiyoruz

df.columns=["FLAG_"+columns if "INS" in columns else "NO_FLAG_"+columns for columns in df.columns]

