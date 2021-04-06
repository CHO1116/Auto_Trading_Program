import pyupbit
import numpy as np
import operator

df = pyupbit.get_ohlcv("KRW.BTC")

df['range'] = (df['high'] - df['low']) * 0.032
df['target'] = (df['open'] + df['low'].shift(1))

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'], 1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
print(df)
df.to_csv("20210327.csv")