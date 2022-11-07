import math #importo la libreria math che mi servirà per calcolare il pi greco nella funzione circonferenza

def menu(): #funzione che stampa l'intestazione del programma
        print ("Scegli che operazione vuoi fare:\n")
        print ("1>> Perimetro quadrato\n2>> Circonferenza cerchio\n3>> Perimetro rettangolo\n")

def quadrato(): #funzione per calcolare il perimetro del quadrato
    ins = int(input("Inserisci misura del lato:\n"))
    print("Il perimetro del quadrato è: ", ins*4)

def circonferenza(): #funzione per calcolare la circonferenza del cerhio
    ins = int(input("Inserisci misura del raggio:\n"))
    print("La circonferenza del cerchio è: ", ins*2*(math.pi))

def rettangolo(): #funzione per calcolare il perimetro del rettangolo
        ins = int(input("Inserisci misura dell'altezza:\n"))
        ins2 = int(input("Inserisci misura della base:\n"))
        print ("Il perimetro del rettangolo è: ",(ins*2)+(ins2*2))
