from src.utils.model_object import DataResponse
from http import HTTPStatus
from src.utils.settings import Settings
import pandas as pd 

config = Settings.get_config()  

class SyncService:
    
    def __init__(self):
        self.api_key = config.APIKEY
        
    def sync_projects(self, request):
        
        """
        Sync data projects with the gateway service.
        """
        response = DataResponse()
        list_data =[]
        try:
            
            apikey = request.headers.get("x-api-key")
            if apikey != self.api_key:
                response.status_code = HTTPStatus.UNAUTHORIZED
                response.message = "Unauthorized access - Invalid API key."
                return response
            projects = pd.read_csv('src/storage/projectos_vivienda.csv', encoding="utf-8")
            for index, row in projects.iterrows():
                data = {
                    'name': row['name'],
                    'logo': row['logo'],
                    'location': row['location'],
                    'city': row['city'],
                    'company': row['company'],
                    'address': row['address'],
                    'contact': row['contact'],
                    'area': row['area'],
                    'price': row['price'],
                    'type': row['type'],
                    'img_url': row['img_url'],
                    'description': row['description'],
                    'url_website': row['url_website'],
                    'latitude': row['latitude'],
                    'longitude': row['longitude'],
                    'nit': row['nit'],
                    'divipola': row['divipola']
                }
                list_data.append(data)
            count_data = len(list_data)
            response_data = {
                "projects": list_data,
                "count": count_data
            }
            response.status_code = HTTPStatus.OK
            response.message = "Data synced successfully."
            response.data = response_data
            return response  
            
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Internal server error."
            response.error = str(e)
            return response