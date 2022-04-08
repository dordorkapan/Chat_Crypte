import socket
import threading

host = '127.0.0.1'
port = 55555

# Serveur de démarrage
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Listes de clients et leurs Nicknames
clients = []
nicknames = []


def broadcast(message):
  """
  Où nous envoyons le message à tous les clients
  """
def gerer(client):
  """
  Gérer les clients qui sont entrain d'arriver
  """
def recevoir():
  """
  Reçoit des clients et ses messages
  """
