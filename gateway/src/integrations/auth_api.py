import requests


class AuthAPI:
    def __init__(self, auth_service_url):
        self.auth_service_url = auth_service_url

    def get_user_data(self, auth_token):
        """
        Get user data from the auth service using the provided token.
        """
        url = f"{self.auth_service_url}/api/v1/auth/get-user"
        token = auth_token.split(" ")[1] if " " in auth_token else auth_token
        
        body = {
            "access_token": token,
            "token_type": "Bearer"
        }
        try:
            response = requests.post(url, json=body)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:

            return {"error": str(e)}  # Return error message and status code


    