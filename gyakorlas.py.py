import random
import math
## véletlen számok generálása




"Generálj 5 véletlen lottószámot [1,90]"
def feladat1():
    i: int = 0
    while i < 5:
        szam: int = math.floor(random.random() * 89+1)
        print(szam, end=" ")
        i += 1




    #2.feladat
    #generálj egy random számot , döntsde el róla hogy páros vagy páratan
def feladat2():
    i:int=0
    while i<1:
        szam:int=math.floor(random.random()*89+10)
    if szam % 2 ==0:
        print("páros")
    else:
        print("Páratlan")
        i+=1




    #3.feladat
    #generálj 15 db egész számot [0,1] között, hány 1 generált?





    #4.generálj véletelen számot 1 és 10 között
    #szorozd meg 3 mal
    #vonj ki belőle 15-öt
    #oszd el 6-tal
    #szorozd meg 2-vel
    #vond ki belőle az eredeti számot
    #A program írja ki, hogy az eredmény egynelő-e 5-tel?




    #5. feladat
    #Irj metódust, mely a paraméterben kapott szövegnek kiirja a hosszát
    # az 5. karakterét nagybetűvel
