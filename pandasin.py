#!/usr/bin/env python
# encoding: utf-8
import pymysql.cursors
import  pandas   as pd
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
plotly.tools.set_credentials_file(username='templarz', api_key='PtKMjV9gAzINZqmQRU4T')
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='900',db='native1',charset='utf8')
cursor=conn.cursor()
cursor.execute("select x,y,z from jdb1 group by x,y,z")
res=cursor.fetchall()
str(res)[0:300]
df=pd.DataFrame( [[j for j in i] for i in res] )
df.rename(columns={0:'x',1:'y',2:'z'},inplace=True);
print (df.head())
trace1=Scatter(
   x=df['x'],
   y=df['y']
)
trace2=Scatter(
   x=df['x'],
   y=df['z']
)
data=Data([trace1,trace2])
py.plot(data,filename='plotly绘图')

