# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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

# écoute 100 connexions actives.
server.listen(100)

list_of_clients = []

def clientthread(conn, addr):
    """
    La fonction diffuse les messages des clients s'il y en a un.
    """
    # envoie un message au client dont l'objet utilisateur est conn
    conn.send("Bienvenue dans le CAT! le Chat Cripte!".encode())
    
    while True:
        try:
            message = conn.recv(2048)
            if message:
                print ("<" + addr[0] + "> " + message)
    			# Appelle la fonction broadcast pour envoyer un message à tous
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection):
    """
    le programme diffuse le message à tous les clients 
    dont le sujet n'est pas le même que celui qui envoie le message
    """
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                # si le lien est cassé, on supprime le client
                remove(clients)

def remove(connection):
    """
    La fonction suivante supprime simplement l'objet 
    de la liste qui a été créée au début de le programme
    """
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
	conn, addr = server.accept()
	list_of_clients.append(conn)

	# imprime l'adresse de l'utilisateur qui vient de se connecter
	print (addr[0] + " connected")

	# crée un thread individuel pour chaque utilisateur qui se connecte
	start_new_thread(clientthread,(conn,addr))	

conn.close()
server.close()
