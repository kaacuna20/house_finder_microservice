from src.utils.settings import Settings

config = Settings.get_config()


class Router:
    """Router class to manage service URLs."""
    project = config.PROJECT_SERVICE_URL
    auth = config.AUTH_SERVICE_URL
    scraping = config.SCRAPING_SERVICE_URL

    def get_service(self, service):
        
        if service == "projects":
            return self.project
        elif service == "auth":
            return self.auth
        elif service == "scraping":
            return self.scraping
        else:
            return None
    