import socket
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Utilisation correcte : script, adresse IP, numéro de port")
	exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))


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
