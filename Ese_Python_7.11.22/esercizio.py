#importo tutte le funzioni che ho svolto sul modulo_operazioni che mi serviranno per far funzionare il mio programma:
from modulo_operazioni import quadrato
from modulo_operazioni import circonferenza
from modulo_operazioni import rettangolo
from modulo_operazioni import menu


menu() #richiamo la funzione menu che mi stamperà l'intestazione della mia applicazione

x = int(input("Inserisci il numero corrispondente all'operazione desiderata:\n")) #faccio inserire all'utente il numero per scegliere la rispettiva operazione collegata

if(x==1):
        print ("Hai scelto di calcolare il perimetro del quadrato\n")
        quadrato() #se l'utente digita 1 viene richiamata la funzione che calcola il perimetro del quadrato

elif(x==2):
        print ("Hai scelto di calcolare la circonferenza del cerchio\n")
        circonferenza() #se l'utente digita 2 viene richiamata la funzione che calcola la circonferenza del cerchio

elif(x==3):
        print ("Hai scelto di calcolare il perimetro del rettangolo\n")
        rettangolo() #se l'utente digita 3 viene richiamata la funzione che calcola il perimetro del rettangolo

else:
        print ("Hai sbagliato a digitare e quindi esci dal programma\n") #se l'utente sbaglia a digitare