# Projet Docker et Architecture Microservices

Ce repository contient le code développé lors de la semaine dédiée à Docker et à l'architecture microservices. Les exercices progressent de la mise en place d'une communication simple entre deux serveurs à la création d'un environnement complet de microservices, tous interagissant de manière décentralisée.

## Objectifs Généraux

### Communication entre Microservices (Exercices 1 à 4)

Les exercices 1 à 4 visent à établir une communication efficace entre microservices, avec des étapes successives :

1. **Ping Pong (Exercice 1):** Communication simple entre deux serveurs via des requêtes HTTP "ping" et "pong".

2. **Annuaire (Exercice 2):** Introduction d'un serveur central pour gérer les adresses des microservices, résolvant le problème de communication lorsque les adresses ne sont pas connues à l'avance.

3. **Docker (Exercice 3):** Dockerisation des microservices pour assurer portabilité et isolation. Les serveurs continuent à communiquer même dans des conteneurs Docker.

4. **Message Broker (Exercice 4):** Intégration d'un serveur de courtier de messages pour déléguer la communication entre les microservices, éliminant la communication directe entre eux.

### Gestion avec Docker Compose (Exercices 1 à 3)

Les exercices d'automatisation utilisent Docker Compose pour simplifier la gestion des conteneurs Docker.

1. **Docker Compose (Exercice 1):** Création d'un fichier `docker-compose.yml` pour lancer tous les microservices avec la commande `docker-compose up`.

2. **Mise à l'échelle (Exercice 2):** Modification de `docker-compose.yml` pour lancer plusieurs instances des serveurs "ping" et "pong", testant ainsi la communication à une plus grande échelle.

3. **Gateway (Exercice 3):** Introduction d'un serveur gateway pour gérer la communication entre plusieurs instances du serveur "ping" et une seule instance du serveur "pong". Cette approche permet d'adapter la communication à différentes configurations de microservices sans modifier leur code.
