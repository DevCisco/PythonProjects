#Calcolo dell'interesse composto
principal=int(input("Inserire il capitale iniziale: "))
rate=int(input("Inserire la percentuale annua: "))
rate=rate/100
x=int(input("Inserire il numero di anni dell'investimento: "))
x+=1
for year in range(1,x):
    amount=principal*(1+rate)**year
    print(f'{year:>2}{amount:>10.2f}')