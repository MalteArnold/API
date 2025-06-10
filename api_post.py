import requests

# API-Endpunkt definieren
url = "https://jsonplaceholder.typicode.com/posts"

# Daten definieren
payload = {
    "title": "Lernen von API Calls",
    "body": "Das ist mein erster POST-Request!",
    "userId": 1,
}

# POST-Anfrage senden
response = requests.post(url, json=payload)

# Antwort prüfen
if response.status_code == 201:
    print("Daten erfolgreich gesendet!")
    print("Antwort:", response.json())
else:
    print("Fehler beim Senden:", response.status_code)
