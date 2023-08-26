import pandas as pd

fruit_list = {
  'Apples': [35,41],
  'Bananas': [21,34]
}

df = pd.DataFrame(fruit_list, index=['2017 Sales', '2018 Sales'])
df.to_csv('fruit.csv')
print(df)