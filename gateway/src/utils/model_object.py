

class DataResponse:
    message: str = ""
    data: dict | list= {}
    status_code: int = 200
    error: str = None

