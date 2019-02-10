import requests


class SlackCLI:

    def __init__(self, webhook):
        self.webhook = webhook

    def send_message(self, message):
        try:
            r = requests.post(url=self.webhook, json={
                "text": message
            })
        except requests.RequestException:
            return False
        return r.status_code == 200
