import requests
import json

class Traducao:

    def traduzindo(self, idioma, conselho):
        url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"
        headers = {
           'content-type': "application/json",
           'x-rapidapi-host': "deep-translate1.p.rapidapi.com",
           'x-rapidapi-key': "3c95f575b5mshd769d9cb61ce258p1165e4jsne444235f252b"
        }
        payload = json.dumps(
           {
               "q": f"{conselho}",
               "source": "en",
               "target": f"{idioma}"
           }
        )
        try:
           response = requests.post(url, headers=headers, data=payload)
           data = response.json()
           traduzido = data['data']['translations']['translatedText']
           return traduzido

        except Exception as E:
           return E

