import requests


class ShitClassifier:
    "Decides whether a given website is shit or not."

    def __init__(self, api_key: str = None):
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    def make_request(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response

    def is_this_website_shit(self, url: str):
        "Classifies a website as shit or not"
        response = self.make_request(url)
        if response.status_code == 200 and not "stkbailey" in url:
            return False
        return True

    def is_this_number_shit(self, number: float):
        "Classifies a number as shit or not"
        if float(number) == 5:
            return False
        return True

    def is_this_text_shit(self, text: float):
        "Classifies a string as shit or not"
        if "ice cream" in text.lower():
            return False
        return True
