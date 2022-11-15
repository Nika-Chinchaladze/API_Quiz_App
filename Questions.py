import requests


class ImportQuestion:
    def __init__(self):
        self.address = "https://opentdb.com/api.php?amount=10&category=27&type=boolean"

    def import_questions(self) -> list:
        response = requests.get(url=self.address)
        response.raise_for_status()
        data = response.json()
        return data['results']
