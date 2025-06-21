import requests
from src.utils.settings import Settings

config = Settings.get_config()


class ScrapingAPI:
    def __init__(self):
        self.base_url = config.PROXY_URL
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': config.APIKEY
        }

    def get_data(self):
        """
        Fetch data from the scraping API.
        """
        url = f"{self.base_url}api/v1/scraping/sync/house-projects"
        response = requests.post(url, headers=self.headers)
        
        return response.json()
