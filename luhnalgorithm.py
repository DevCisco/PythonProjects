def verificaluhn():
    somma=0
    x=15
    n=[]
    for i in range(0,x):
        element=int(input("Inserire la cifra della carta: "))
        if i==x-1:
            somma+=element
            continue
        if (i%2)==0:
           element=element*2
           if element>=10:
                element=(element%2)+1
        somma=somma+element
    z=int(input("Inserire l'ultima cifra della carta: "))
    y=somma%10
    if ((10-y)==z):
        print("Corretto")
    else:
        print("Non corretto, inserire nuovamente il numero")
        verificaluhn()

def main():
    verificaluhn()

if __name__ == '__main__':
    main()
