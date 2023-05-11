import pandas as pd
import re

df=pd.read_csv('NorthWales.csv', skiprows=range(1))

#Convert every "No data" with value 0 since it doesn't count in the average
df=df.replace("No data", 0)

#Rename every column like "Name.N" to "Name"
patterns=['^(Status)\.?\d*$','^(Nitrogen dioxide)\.?\d*$', '^(Nitrogen oxides as nitrogen dioxide)\.?\d*$']
new_names=['Status', 'Nitrogen dioxide', 'Nitrogen oxides as nitrogen dioxide']
rename_dict={}

for pattern, new_name in zip(patterns, new_names):
    regex_pattern=re.compile(pattern)
    matching_cols=[col for col in df.columns if regex_pattern.match(col)]
    for col in matching_cols:
        rename_dict[col]=new_name
df=df.rename(columns=rename_dict)

#Drop the Status columns since it doesnt provide further information about pollutant
df=df.drop('Status', axis=1)
df=df.drop('Date', axis=1)

#Get Nitrogen dioxide columns
nd_cols=df.filter(like="Nitrogen dioxide")
#Compute average of columns
nd_avg=nd_cols.mean(axis=1)
#Rename nitrogen dioxide average column
nd_avg.name="Nitrogen dioxide average"

#Replace the nitrogen dioxide columns with the average
df=df.drop(nd_cols.columns, axis=1)
df=pd.concat([df, nd_avg], axis=1)

df.head()