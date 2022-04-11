import socket
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# vérifie si suffisamment d'arguments ont été fournis
if len(sys.argv) != 3:
    IP_address = "172.20.12.20"
    Port = 2222
else:
    # prend le premier argument de l'invite de commande comme adresse IP
    IP_address = str(sys.argv[1])
    
    # prend le deuxième argument de l'invite de commande comme numéro de port
    Port = int(sys.argv[2])
"""
# vérifie si suffisamment d'arguments ont été fournis
if len(sys.argv) != 3:
	print ("Utilisation correcte : script, adresse IP, numéro de port")
	exit()

# prend le premier argument de l'invite de commande comme adresse IP
IP_address = str(sys.argv[1])

# prend le deuxième argument de l'invite de commande comme numéro de port
Port = int(sys.argv[2])
"""

#lie le serveur à une adresse IP saisie et à la numéro de port spécifié.
server.bind((IP_address, Port))

def send_msg(sock):
    """
    Le programme reçoit un message que vous écrivez, l'envoie à l'autre client et l'affiche sur votre écran
    """
    while True:
        data = sys.stdin.readline()
        #encrypt 
        sock.send(data.encode())
        sys.stdout.write("<You>")
        sys.stdout.write(str(data))
        sys.stdout.flush()

    
start_new_thread(send_msg,(server,))

while True:
    message = server.recv(2048)
    #decrypt
    print (message)


server.close()
