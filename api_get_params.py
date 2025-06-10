import requests

# API url der Kategorien
url_categories = "https://api.chucknorris.io/jokes/categories"

# GET-Anfrage senden
response_categories = requests.get(url_categories)

# Status prüfen
if response_categories.status_code == 200:
    # JSON-Daten extrahieren
    categories_data = response_categories.json()
    print("Kategorien: ", categories_data)

    # Kategorie abfragen
    choosen_category = input("Wähle eine Kategorie: ")

    # API-Endpunkt definieren
    url = "https://api.chucknorris.io/jokes/random"

    # Parameter Kategorie definieren
    params = {"category": choosen_category}

    # GET-Anfrage senden
    joke_response = requests.get(url, params=params)

    # Status prüfen
    if joke_response.status_code == 200:
        # JSON-Daten extrahieren
        joke = joke_response.json()
        print(
            f"Chuck Norris Witz in der Kategorie '{choosen_category}':\n{joke['value']}"
        )
    else:
        print("Fehler beim API-Aufruf:", joke_response.status_code)
else:
    print("Fehler beim API-Aufruf:", response_categories.status_code)
