def get_info():
    print("Witaj! To jest kalkulator.")  

def dodaj(a,b):
    wynik = a + b
    return wynik

def odejmij(a,b):
    return a-b
    
get_info()   
a = int(input())   
b = int(input()) 

print(dodaj(a, b))

print("Koniec programu")