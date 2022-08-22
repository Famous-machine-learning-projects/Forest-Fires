import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
%matplotlib inline

df = pd.read_csv('forestfires.csv', encoding='cp1252')
df.head()
df.describe()
cdf = df[['X', 'Y','FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']]
from scipy.stats import yeojohnson
yf_target, lam = yeojohnson(df["area"])
df['yf_target']=yf_target
df['lam']=lam

cdf = df[['X', 'Y','FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area', 'yf_target', 'lam']]
cdf.head(1000)

plt.scatter(cdf.temp, cdf.area,  color='blue')
plt.xlabel("Y")
plt.ylabel("area")
plt.show()

plt.scatter(cdf.temp, cdf.yf_target,  color='red')
plt.xlabel("Y")
plt.ylabel("yf_target")
plt.show()

plt.scatter(cdf.temp, cdf.lam,  color='green')
plt.xlabel("Y")
plt.ylabel("lam")
plt.show()
