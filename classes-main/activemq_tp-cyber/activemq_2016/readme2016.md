CVE 2016-3088

<img width="992" alt="Capture d’écran 2024-10-31 à 19 28 54" src="https://github.com/user-attachments/assets/e20e4588-3776-4320-a3bb-e73a6db35405">

Pour commencer, lancez ActiveMQ en arrière-plan dans le dossier activemq_2016 en utilisant:
docker compose up -d

![Capture d’écran 2024-10-28 à 11 32 42](https://github.com/user-attachments/assets/78ec3caa-2c74-45b7-b19a-9ccc136e4e9c)

Accédez ensuite à l'interface ActiveMQ dans un navigateur à l'adresse :

http://localhost:8161/admin/

Vous verrez la version d'ActiveMQ, ici (5.11.1) :


![Capture d’écran 2024-10-28 à 11 35 29](https://github.com/user-attachments/assets/0521d85f-f8ac-4fa0-b8b6-427b2bc320f9)

On peut aussi voir la version de activemq dans le fichier docker-compose.yml:

![Capture d’écran 2024-10-28 à 11 38 12](https://github.com/user-attachments/assets/52a231f2-a055-442a-b362-cec6ed79b7bd)
Le suffixe with-cron dans l'image vulhub/activemq:5.11.1-with-cron indique que le conteneur ActiveMQ inclut le service cron pour exécuter automatiquement des tâches planifiées. comme des scripts ou des commandes à des moments précis dans le conteneur.

Pour scanner le réseau afin d'identifier les services actifs et leurs versions avec la commande :
nmap -p- 192.168.1.145

![Capture d’écran 2024-10-28 à 12 32 29](https://github.com/user-attachments/assets/adf66034-e307-4601-8485-cc26b76d2a32)

Pour exploiter la vulnérabilité, exécutez le script CVE-2016-3088.py :

python3 CVE-2016-3088.py -u http://localhost:8161/ 

![Capture d’écran 2024-10-28 à 11 45 24](https://github.com/user-attachments/assets/c34cc77c-42b1-4d43-9c97-e98e63946e14)

Si l’exploit réussit, vous pouvez accéder au shell en utilisant l’URL suivante :

http://localhost:8161/api/evil.jsp?pwd=9527&i=whoami

Nous avons ca:

![Capture d’écran 2024-10-28 à 11 47 17](https://github.com/user-attachments/assets/9b6de1b9-f5a5-470c-b8b9-0faf53f3d8b4)

cela prouve bien que nous somme en root et nous avons infiltré active grace au webshell

Changer whoami par n'importe quelle commande pour voir le résultat. Par exemple, pour afficher les fichiers :
![Capture d’écran 2024-10-28 à 11 49 15](https://github.com/user-attachments/assets/2b1241fb-b26f-4f18-abff-4db980a52eb0)


Cet exploit illustre l'impact de CVE-2016-3088, permettant un accès total au serveur ActiveMQ via un WebShell malveillant.

