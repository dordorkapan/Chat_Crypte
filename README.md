# Cat: Le Chat Crypté

Dans ce projet, je vais créer un chat entre deux ordinateurs, en les connectant via leur adresse IP. Ici, les clients communiquent avec le serveur, et donc à travers lui, ils communiquent entre eux. Tandis que le chat va être crypté et seulement avec la clé, vous pouvez lire le message. 

## Décomposition en sous-problèmes:

- Connecter les deux ordinateurs via leur adresse IP
- Création l'espace de chat
- Convertir le texte soumis en un texte crypté


## MVP
- Premièrement, j'attend a créé une simple discussion entre deux ordinateurs, en les connectant via leur adresse IP
- Deuxièmement, fair cette chat crypté
- Troisièmement, ajouter GUI (graphical user interface)

## Présentation des structures de donénes utilisées:

### Le Server
```
def clientthread(conn, addr):
"""
La fonction diffuse les messages des clients s'il y en a un.
"""

def broadcast(message, connection):
"""
La fonction diffuse le message à tous les clients 
dont le sujet n'est pas le même que celui qui envoie le message
"""
def remove(connection):
"""
La fonction suivante supprime simplement l'objet 
de la liste qui a été créée au début de
le programme
"""
```

### Le Client
```
def send_msg(sock):
"""
Le programme reçoit un message que vous écrivez, l'envoie à l'autre client et l'affiche sur votre écran
"""
```

### Inspiration:
-  Deepak Srivatsav sur GeeksforGeeks
