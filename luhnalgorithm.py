import time
def verificaluhn():
    somma=0
    x=16
    for i in range(x-1):
        element=int(input("Inserire la cifra della carta: "))
        if (i%2)==0:
           element=element*2
           if element>=10:
                element=element-9
        somma+=element
    z=int(input("Inserire l'ultima cifra della carta: "))
    y=somma%10
    if (((10-y)%10)==z):
        print("Corretto")
    else:
        print("Non corretto, inserire nuovamente il numero")
        verificaluhn()

def main():
    verificaluhn()

if __name__ == "__main__":
    main()
