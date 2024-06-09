import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())


unique_values = data['whoAmI'].unique()
one_hot_data = pd.DataFrame({value: (data['whoAmI'] == value).astype(int) for value in unique_values})
print(one_hot_data.head())