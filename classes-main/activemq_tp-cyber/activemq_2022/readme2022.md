CVE 2022-32207

Pour commencer, lancez ActiveMQ en arrière-plan dans le dossier activemq_2022 en utilisant:
docker compose up -d

![Capture d’écran 2024-10-29 à 12 50 29](https://github.com/user-attachments/assets/4b41d643-0f8f-428c-8947-7d262ad6d675)

Accédez ensuite à l'interface ActiveMQ dans un navigateur à l'adresse :

http://localhost:8161/admin/

Vous verrez la version d'ActiveMQ, ici (5.17.3) :

![Capture d’écran 2024-10-29 à 12 51 24](https://github.com/user-attachments/assets/e3102a17-2498-43ed-b2f8-6fc7734b9407)

On peut aussi voir la version de activemq dans le fichier docker-compose.yml:

![Capture d’écran 2024-10-29 à 12 52 05](https://github.com/user-attachments/assets/75a8b851-0764-4f93-b1c9-d5dad932761b)


Pour scanner le réseau afin d'identifier les services actifs et leurs versions avec la commande :
nmap -p- 192.168.1.145

![Capture d’écran 2024-10-29 à 12 52 53](https://github.com/user-attachments/assets/25f4b9ef-635b-4b9a-9c9d-45d6ca0e4f06)

Pour exploiter la vulnérabilité CVE-2022-32207, 
