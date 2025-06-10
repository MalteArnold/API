import requests

# API-Endpunkt definieren
url = "https://api.chucknorris.io/jokes/random"

# GET-Anfrage senden
response = requests.get(url)

# Statuscode prüfen
if response.status_code == 200:
    # JSON-Daten extrahieren
    data = response.json()
    print("Chuck Norris Witz:", data["value"])
else:
    print("Fehler beim API-Aufruf:", response.status_code)
