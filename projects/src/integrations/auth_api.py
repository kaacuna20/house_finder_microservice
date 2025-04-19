import requests
from src.utils.settings import Settings

config = Settings.get_config()

class AuthApi:
    def __init__(self):
        self.base_url = config.GATEWAY_URL
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get_user(self, auth_token: str): 
        url = f"{self.base_url}api/v1/auth/get-user"
        
        token = auth_token.split(" ")[1] if " " in auth_token else auth_token
        
        body = {
            "access_token": token,
            "token_type": "Bearer"
        }
        
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    