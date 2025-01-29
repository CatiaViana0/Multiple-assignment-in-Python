if __name__ == '__main__' :
    C, Espaco="*", " "
    A= int (input("Number of lines for the tree "))
    Impar=1
    Inicio=int(((A-1) *2+1)/2)
    for L in range (1, A+1):
        print(Inicio*Espaco, end="")
        print(Impar*C, end="")
        print()
        Impar+=2
        Inicio-=1
                
