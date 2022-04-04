# Chat Crypté

Dans ce projet, je vais créer un chat entre deux ordinateurs, en les connectant via leur adresse IP. Tandis que le chat va être crypté et seulement avec la clé, vous pouvez lire le message.

## Décomposition en sous-problèmes:

- Connecter les deux ordinateurs via leur adresse IP
- Création l'espace de chat
- Convertir le texte soumis en un texte crypté

## Présentation des structures de donénes utilisées:
```
class Client():

  def _init_()

  def clear(): 
    """
    Cette fonction est appelée chaque fois qu'un nouveau message est reçu du serveur.
    """
    
  def connecter_au_serveur(compter):
    """
    Appelé pour essayer de se connecter au serveur
    """
  
  def recevoir():
    """
    Cette fonction gère la tâche de réception des messages du serveur/d'autres clients.
    """
    
  def envoyer_msg():
    """
    Utilisé pour gérer la tâche d'envoyer des messages à la salle de discussion.
    """
    
class Server():

  def gérer_client(client):
  """
  C'est le thread qui écoute toutes les données entrantes par un seul client.
  """

  def close_connection(client, kicked=False):
  """
  Cette fonction est appelée chaque fois qu'un client ou une connexion doit être fermé
  """
  
class Cryptographie():

  def Texte_normal():

```
