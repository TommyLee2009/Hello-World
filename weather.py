# !/usr/bin/python3
# -*-coding:utf-8 -*-
"""
@File : 
@Time : 2020/11/14
@Author : LCY
@Email : XXXX@163.com
@Function : XXXX
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = r'en_climate_hourly_NS_8201780_10-2020_P1H.csv'
weather_10_2020 = pd.read_csv(file,  index_col='Date/Time', parse_dates=True)
print(weather_10_2020.info())
# weather_10_2020['Temp (\xb0C)'].plot(figsize=(15, 5))
# plt.show()
weather_10_2020.columns = [s.replace('\xb0', '') for s in weather_10_2020.columns]
weather_10_2020.dropna(axis=1, how='all', inplace=True)
temperatures = weather_10_2020[['Temp (C)']]
temperatures['Hour'] = weather_10_2020.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()
plt.show()