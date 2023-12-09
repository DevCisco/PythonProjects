from currencylib import *
convlist={"Euro":"euro","US Dollar":"usdollar","Dollaro Canadese":"candollar","Dollaro di Singapore":"singaporedollar","Dollaro Australiano":"ausdollar","Dollaro Neozelandese":"nzdollar","Nuovo Dollaro di Taiwan":"newtwdollar","Peso Argentino":"pesoarg","Riyal Saudita":"saudiriyal","Dirham Emirati Arabi Uniti":"uaedir"}
print("Le valute disponibili sono: ",convlist.keys())
print("I codici delle valute sono:", convlist.values())
x=input("Inserire la valuta: ")
if(x=='euro'):
    euroconv()
if(x=='usdollar'):
    usconv()
if(x=='ausdollar'):
    ausconv()
if(x=='singaporedollar'):
    singaporeconv()
if(x=='candollar'):
    canconv()
if(x=='nzdollar'):
    nzdconv()
if(x=='newtwdollar'):
    newtwdolconv()
if(x=='pesoarg'):
    pesoargconv()
if(x=='saudiriyal'):
    saudiconv()
if(x=='uaedir'):
    uaedirconv()