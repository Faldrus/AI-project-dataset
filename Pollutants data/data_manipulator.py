import pandas as pd

df=pd.read_csv('NorthWales.csv')

df.to_csv('NorthWales.csv', lineterminator='\n')