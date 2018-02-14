import pandas as pd
import  sys as os
import  csv
import  lxml
import  html5lib
import matplotlib
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_html("https://www.gfmag.com/global-data/economic-data/countries-highest-gdp-growth")[0]
#df.columns = df.iloc[0]
#df = df.reindex(df.index.drop(0))
#print(df.head())
#print(df.shape)

converted_column8 = pd.to_numeric(df['2008'], errors = 'coerce')
converted_column9 = pd.to_numeric(df['2009'], errors = 'coerce')
converted_column10 = pd.to_numeric(df['2010'], errors = 'coerce')
converted_column11 = pd.to_numeric(df['2011'], errors = 'coerce')
converted_column12 = pd.to_numeric(df['2012'], errors = 'coerce')
converted_column13 = pd.to_numeric(df['2013'], errors = 'coerce')
converted_column14 = pd.to_numeric(df['2014'], errors = 'coerce')
converted_column15 = pd.to_numeric(df['2015'], errors = 'coerce')
converted_column16 = pd.to_numeric(df['2016'], errors = 'coerce')
converted_column17 = pd.to_numeric(df['2017'], errors = 'coerce')
df['Country']
df['2008'] = converted_column8
df['2009'] = converted_column9
df['2010'] = converted_column10
df['2011'] = converted_column11
df['2012'] = converted_column12
df['2013'] = converted_column13
df['2014'] = converted_column14
df['2015'] = converted_column15
df['2016'] = converted_column16
df['2017'] = converted_column17

#print(df[['Country','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']].head())
df[['Country','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']].head()
#df.set_index('Country')
#df = df.index.drop(10)
df.set_index('Country')
del df['Avg % GDP change']
#print( pd.melt( df,value_vars=['Country']))
df = pd.DataFrame(df, columns=['Country','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017'])
#print(df.unstock)
melted = pd.melt(df, id_vars=['Country'],
                 var_name="Years", value_name="GDP")

#seaborn plots
#seaborn plots
cd=pd.to_numeric(melted['GDP'], errors = 'coerce')
melted['GDP']=cd
sns.lmplot(x='Years', y='GDP', data=melted, fit_reg=True,hue='Country' ,palette='Set1')
plt.show()


#sns.lmplot(x="Years", y="GDP" ,hue="Country", data=melted , palette="Set1");
"""
x = melted['Country']
y = melted['Years']
z = melted['GDP']
df1 = df({'x': x, 'y': y, 'z': z})

# Plot with palette
sns.lmplot(x='x', y='y', data=df1, fit_reg=False, hue='x', legend=False, palette="Blues")

# reverse palette
sns.lmplot(x='x', y='y', data=df1, fit_reg=False, hue='x', legend=False, palette="Blues_r")

#print(melt_data)"""





""""
melt_data = pd.melt(melted, id_vars=['Years'],var_name='Country')
melt_data.rename(columns={'value':'GDP'}, inplace=True)
sns.lmplot(x="Years", y="GDP", hue="Country", data=melt_data, palette="Set1");


print(melted)"""


