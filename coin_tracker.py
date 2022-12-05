from tkinter import *
import time
import json
import requests
from tkinter import ttk
import pyautogui as p
import winsound
root = Tk()
root.title("Coin Tracker")
root.geometry("400x400")
root.maxsize(400,400)
root.minsize(400,400)
value_label = Label(root, text="")
value_label.place(x=0,y=150)
coinlist=["BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","ADAUSDT","XRPUSDT","DOTUSDT","USDCUSDT","DOGEUSDT","SHIBUSDT","AVAXUSDT","LUNAUSDT","LTCUSDT","BUSDUSDT","UNIUSDT","LINKUSDT","ALGOUSDT","BCHUSDT","MATICUSDT","VETUSDT","XLMUSDT","AXSUSDT","MANAUSDT","ICPUSDT","TRXUSDT","FTTUSDT","USTUSDT","FILUSDT","DAIUSDT","ETCUSDT","EGLDUSDT","ATOMUSDT",
"THETAUSDT","HBARUSDT","NEARUSDT","FTMUSDT","XTZUSDT","GRTUSDT","XMRUSDT","HNTUSDT","EOSUSDT","SANDUSDT","KLAYUSDT","FLOWUSDT","CAKEUSDT","AAVEUSDT","XECUSDT","KDAUSDT","LRCUSDT","KSMUSDT","NEOUSDT","MKRUSDT","QNTUSDT","ENJUSDT","CHZUSDT","RUNEUSDT","ONEUSDT","STXUSDT","WAVESUSDT","BTTUSDT","HOTUSDT","AMPUSDT","ZECUSDT","ARUSDT","DASHUSDT","COMPUSDT","CELOUSDT","CRVUSDT","NEXOUSDT","IOTXUSDT","TFUELUSDT","WAXPUSDT",
"XEMUSDT","BATUSDT","DCRUSDT","ICXUSDT","QTUMUSDT","OMGUSDT","TUSDUSDT","MINAUSDT","YFIUSDT","RVNUSDT","VGXUSDT","SUSHIUSDT","UMAUSDT","AUDIOUSDT","SCRTUSDT","ZILUSDT"]
key = "https://api.binance.com/api/v3/ticker/price?symbol="
cbox=ttk.Combobox(root,values=coinlist)
cbox.place(x=25,y=0)
state=["HIGHER","LOWER","NONE"]
cbox_state=ttk.Combobox(root,values=state)
cbox_state.place(x=25,y=100)
currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT","BNBUSDT"]
warn=Entry(root)
cbox_state.current(2)
warn.place(x=25,y=50)
def get_warn():
    x=float(warn.get())
    return x
def get_value():
    try:        
        url=key+cbox.get()
        data = requests.get(url)
        data = data.json()
        price=data["price"]
        float_price=float(price)
        value_label.config(text=f"{data['symbol']} price is {data['price']}",font=("Arial",12,"bold"))
        if cbox_state.get()=="HIGHER" and get_warn()<float_price:
            winsound.Beep(5000, 3000)
            check=p.confirm("Warning your coin is higher than {}".format(get_warn()),buttons=["Okay"])
            cbox_state.current(2)         
        if cbox_state.get()=="LOWER" and get_warn()>float_price:
            winsound.Beep(5000, 3000)
            check=p.confirm("Warning your coin is lower than {}".format(get_warn()),buttons=["Okay"])
            cbox_state.current(2)            
    except:KeyError
    root.after(1000,get_value)   
root.after(1000,get_value)
root.mainloop()