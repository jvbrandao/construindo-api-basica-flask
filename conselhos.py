import requests

class Conselhos:
    def conselho(self):
        r = requests.get('https://api.adviceslip.com/advice')
        conselho = r.json()
        advice = conselho['slip']['advice']

        conselho = conselho['slip']['advice']
        return conselho
