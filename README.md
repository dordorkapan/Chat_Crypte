# Cat: Le Chat Crypté

Dans ce projet, je vais créer un chat entre deux ordinateurs, en les connectant via leur adresse IP. Ici, les clients communiquent avec le serveur, et donc à travers lui, ils communiquent entre eux. Tandis que le chat va être crypté et seulement avec la clé, vous pouvez lire le message. 

## Décomposition en sous-problèmes:

- Connecter les deux ordinateurs via leur adresse IP
- Création l'espace de chat
- Convertir le texte soumis en un texte crypté

## MVP
Premièrement j'attend a créé une simple discussion entre deux ordinateurs, en les connectant via leur adresse IP

## Présentation des structures de donénes utilisées:

### Le Server

```
def broadcast(message):
  """
  où nous envoyons le message à tous les clients
  """
def gerer(client):

def recevoir():

```

### class Client():

```
  def _init_(self, host, port):
  
  def gui_loop(self):
  
  def ecrire(self):
  
  def cripter(self, message):
  
  def arreter(self):
  
  def recevoir(self):
```
