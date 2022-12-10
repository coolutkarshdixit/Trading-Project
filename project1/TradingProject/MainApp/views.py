from django.shortcuts import render
from django.http import HttpResponse
import pandas

# Create your views here.
def home(request):
    

    df=pandas.read_csv(r'/Users/utkarsh/Desktop/project/TradingProject/NIFTY_F1_Xm8mAtb.csv')
    Candle=df.loc[:,[ "BANKNIFTY","OPEN","HIGH","LOW","CLOSE","DATE"]]
    jsn=Candle.to_json()

    print(jsn)
    f=open("/Users/utkarsh/Desktop/project1/TradingProject/static/file.json","w")
    f.write(jsn)

    f.close()
    
    return render(request,"file.html")
