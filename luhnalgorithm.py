def verificaluhn():
    somma=0
    x=16
    n=[]
    for i in range(0,x):
        element=int(input("Inserire la cifra della carta: "))
        n.insert(i,element)
    print("ciccio", n)
    for i in range (x,0):
        if i%2==0:
            n[i]=n[i]*2
            if n[i]>10:
                n[i]=(n[i]%2)+1
    for num in n:
       somma=somma+num
    if ((somma%10)==0):
        print("Corretto")
    else:
        print("Non corretto, inserire nuovamente il numero")
        verificaluhn()

def main():
    verificaluhn()

if __name__ == '__main__':
    main()
