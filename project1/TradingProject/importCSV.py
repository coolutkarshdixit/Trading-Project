import pandas as pd

Candle=pd.read_csv(r'/Users/utkarsh/Desktop/project/TradingProject/NIFTY_F1_Xm8mAtb.csv')
jsn=Candle.to_json()

print(jsn)