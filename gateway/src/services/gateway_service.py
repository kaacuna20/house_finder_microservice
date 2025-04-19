import requests
from src.utils.router import Router
from src.utils.serializers import GetItemRoute, CreateLog
from src.utils.normalize_path import normalize_route
from src.services.route_service import RouteTableService
from src.services.activity_log_service import ActivityLogService
from src.integrations.auth_api import AuthAPI
from src.utils.model_object import DataResponse
from http import HTTPStatus

class GatewayService:
    def __init__(self):
        self.router = Router()
        self.auth_api = AuthAPI(self.router.auth)
        self.activy_log_service = ActivityLogService()
        self.route_table_service = RouteTableService()
        
    def proxy(self, request, path):
        
        response = DataResponse()
        method = request.method
        body = request.get_json()
        headers = dict(request.headers)
        query_params = dict(request.args)
        
        try:
            normlize_path = normalize_route(path)  
            data = GetItemRoute(
                path=normlize_path,
                method=method,
            )
            get_route = self.route_table_service.get_route_table(data).data
            
            if not get_route:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Route not found."
                return response
            
            middleware_response = self.middleware(request, get_route[0])
            if middleware_response[0].get("status") != "success":
                response.status_code = middleware_response[1]
                response.data = middleware_response[0].get("error")
                response.message = "failed to authenticate user in middleware!"
                return response   
                
            service = get_route[0].get("service")
            module = get_route[0].get("module")
            action = get_route[0].get("action")
            
            router = self.router.get_service(service)
            if not router:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Service not found."
                return response
            
            endpoint = f"{router}{path}"
  
            # response_api = {
            #     "method": method,
            #     "url": endpoint,
            #     "headers": headers,
            #     "params": query_params,
            #     "json": body,
            #     "service": service,
            #     "module": module,
            #     "action": action,
                
            # }          
            response_api = requests.request(
                method=get_route[0]["method"],
                url=endpoint,
                headers=headers,
                params=query_params,
                json=body
            )
            self.activy_log_service.create_activity_log(
                CreateLog(
                    name="Gateway Service",
                    service=service,
                    causer=middleware_response[0].get("user")['email'] if middleware_response[0].get("user") else "",
                    action=action,
                    data={
                        "path": path,
                        "method": method,
                        "module": module,
                        "request":{
                            "method": method,
                            "url": endpoint,
                            "headers": headers,
                            "params": query_params,
                            "json": body,
                        },
                        "response": response_api.json(),
                    }
                )
            )
            response.data = response_api.json()['data']
            response.status_code = response_api.json()['status_code']
            response.message = response_api.json()['message']
            response.error = response_api.json()['error'] if response_api.json().get('error') else None
            return response
        
        except requests.exceptions.RequestException as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error connecting to the service from Gateway."
            response.error = str(e)
            return response
        
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error processing the request from Gateway."
            response.error = str(e)
            return response
        
    
    def middleware(self, request, route_info):
        """
        Middleware to handle authentication and authorization for the gateway service.
        """
        
        is_authenticated = route_info.get("is_authenticated")
        if is_authenticated is False:
            return {"status": "success", "user": ""}, HTTPStatus.OK
            
        auth_token = request.headers.get("Authorization")
        if not auth_token:
            return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        
        user = self.get_user_authenticate(auth_token)
        if user['error']:
            return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        
        service = route_info.get("service")
        module = route_info.get("module")
        action = route_info.get("action")
        
        if not module:
            return {"error": "Module not specified"}, HTTPStatus.BAD_REQUEST
        if not service:
            return {"error": "Service not specified"}, HTTPStatus.BAD_REQUEST
        if not action:
            return {"error": "Action not specified"}, HTTPStatus.BAD_REQUEST
        
        if not self.validate_permission(user, module, service, action):
            return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        
        return {"status": "success", "user": user}, HTTPStatus.OK 
    
    def get_user_authenticate(self, token):
        user_data = self.auth_api.get_user_data(token)#request.headers.get("Authorization"))
        if user_data.get("error"):
            return {"error": user_data.get("error")}
        
        user = {
            "user_id": user_data.get("data")["id"],
            "email": user_data.get("data")["email"],
            "is_active": user_data.get("data")["is_active"],
            "is_superuser": user_data.get("data")["is_super_user"],
            "permissions": user_data.get("data")["role"]["permissions"],
            "role": user_data.get("data")["role"]["reference"],
            "error":None,
        }
        
        return user
        
    def validate_permission(self, user, module, service, action):
        """
        Validate if the user has permission to access the requested module and service.
        """
        
        user_permisions = user.get("permissions")
        if not user_permisions:
            return False
        
        if user.get("is_super_user") == 1:
            return True
        
        for permision in user_permisions:
            if service in permision.keys():
                service_data = permision[service]
                if module in service_data.keys():
                    actions = service_data[module]
                    if action in actions:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        

        



