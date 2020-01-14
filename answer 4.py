# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:27:25 2020

@author: yzzhj
"""
import pandas as pd
import datetime
from dateutil.parser import parse
data = pd.read_excel('C:/Users/yzzhj/Desktop/dataset.xlsx',sheet_name = 'dataset1', header = None)
data.columns = ['id','trading date','mktcap value']
date = data['trading date'].apply(lambda x: str(x)).apply(lambda x: parse(x))
data['new date']=date
df = data.set_index('new date')
df_empty = pd.DataFrame(columns=['id', 'trading date', 'mktcap value'])
for i in (df['id'].unique()):
    dfg = df[df['id']==i]
    a = dfg.groupby(pd.TimeGrouper('M'))
    k = a.tail(1)
    b = k._stat_axis.values.tolist()
    b = pd.to_datetime(b)
    data1 = data[data['id']==i]
    data1['m'] = data1['new date'].map(lambda x: x.month)
    df1 = df[df['id']==i]
    for i in range(0,len(k)):
        f = k.iloc[i].isnull()['mktcap value']
        c = data1[data1['new date']==b[i]-datetime.timedelta(days=1)].isnull()['mktcap value']
        t = data1[data1['m']==b.map(lambda x:x.month)[i]].isnull()['mktcap value'].all()
        test = list(data1['new date'])
        if t:
            dfgg = df1.groupby(pd.TimeGrouper('M'))
            z = dfgg.tail(1)
            print(z)
        elif f:
            if c.any():
                df = df
            else:
                df1.drop(index = [b[i]], inplace = True)
                dfgg = df1.groupby(pd.TimeGrouper('M'))
                z = dfgg.tail(1)
                print(z)