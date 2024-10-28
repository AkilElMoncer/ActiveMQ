CVE 2023-46604

Pour commencer, lancez ActiveMQ en arrière-plan dans le dossier activemq_2023 en utilisant Docker Compose :

docker compose up -d

![Capture d’écran 2024-10-28 à 12 38 08](https://github.com/user-attachments/assets/d8f89a89-5db4-443e-ac48-01ada7163acd)

Accédez ensuite à l'interface d'administration dans un navigateur à l'adresse :

http://localhost:8161/admin/

Vous verrez la version d'ActiveMQ, ici (5.17.3) :

![Capture d’écran 2024-10-28 à 12 39 45](https://github.com/user-attachments/assets/1a11852e-ada9-4ece-b2b3-b92e99d1fdbc)

On peut aussi voir la version de activemq dans le fichier docker-compose.yml:

![Capture d’écran 2024-10-28 à 12 40 48](https://github.com/user-attachments/assets/3f82642d-676b-49d2-9f2f-c72d4246717f)

Pour scanner le réseau afin d'identifier les services actifs et leurs versions avec la commande : nmap -p- 192.168.1.145

![Capture d’écran 2024-10-28 à 12 42 12](https://github.com/user-attachments/assets/2377b011-43e0-498a-8ba0-d0a664806038)


