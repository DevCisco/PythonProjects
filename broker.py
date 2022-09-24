def commissione(n):
    n=(n*20)/100
    return n
def commissioneplus(n):
    n=(n*50)/100
    return n
print("Benvenuti nel calcolo delle commissioni del servizio di brokeraggio Andamento Lento")
print("Inserire il valore della plusvalenza:")
plusv=int(input())
if plusv<500:
    print("Nessuna commissione")
if 500<plusv<1000:
    x=commissione(plusv)
    print("La commissione è: ",x)
    plusv=plusv-x
    print("Per un totale di: ",plusv)
if plusv>1000:
    x=commissioneplus(plusv)
    print("La commissione è: ",x)
    plusv=plusv-x
    print("Per un totale di: ",plusv)
