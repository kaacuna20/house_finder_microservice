from os import environ


class BaseConfig:
    SECRET_KEY = environ.get('SECRET_APP_KEY', 'your_secret_key')
    URL_PREFIX = '/api/v1/scraping'
    GATEWAY_URL = environ.get('GATEWAY_URL', 'http://127.0.0.1:5000')
    ALLOW_ORIGIN = {"127.0.0.1", environ.get('GATEWAY_IP')}
    DEBUG = environ.get('DEBUG', True)
    APIKEY = environ.get('SCRAPING_API_KEY', 'your_api_key')
 
 
class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    pass
    
    
class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True

    
class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False  # Disable debug mode in production
    

class Settings:
    """Configuration factory."""
    """@autor:Kevin Acuña,
    @version: v1 09/04/2025
    @description: This class contains the settings for the application.
    """
    environment: str = environ.get("APP_ENV", "development")
    
    @staticmethod
    def get_config():
        env = Settings.environment
        if env == "development":
            return DevelopmentConfig
        elif env == "testing":
            return TestingConfig
        elif env == "production":
            return ProductionConfig
        else:
            raise ValueError(f"Unknown environment: {env}")