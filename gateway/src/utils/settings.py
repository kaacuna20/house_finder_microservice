import os
from os import environ, makedirs
from datetime import datetime

log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, f'{datetime.now().strftime("%Y%m%d")}.log')


class BaseConfig:
    SECRET_KEY = environ.get('SECRET_APP_KEY', 'your_secret_key')
    URL_PREFIX = '/api/v1/gateway'
    DEBUG = environ.get('DEBUG', True)
    PROJECT_SERVICE_URL = environ.get("PROJECT_SERVICE_URL", "http://127.0.0.1:5001/")
    AUTH_SERVICE_URL = environ.get("AUTH_SERVICE_URL", "http://127.0.0.1:5003/")
    SCRAPING_SERVICE_URL = environ.get("SCRAPING_SERVICE_URL", "http://127.0.0.1:5002/")
    CACHE_TYPE = environ.get("CACHE_TYPE", "RedisCache")
    CACHE_REDIS_URL = environ.get("REDIS_URL", "redis://localhost:6379/0")
    CACHE_DEFAULT_TIMEOUT = int(environ.get("CACHE_DEFAULT_TIMEOUT", 300))
    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://flask.logging.wsgi_errors_stream'
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': log_file_path,
                'mode': 'a',
                'encoding': 'utf-8'
            }
        },
        'root': {
            'level': environ.get('LOG_LEVEL', 'DEBUG'),
            'handlers': ['console', 'file']
        }
    }
     
 
class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    MONGO_URI = environ.get('MONGO_URL', 'mongodb://root:password@localhost:27017/gatewaye_db?authSource=admin')
    DB_NAME = environ.get('MONGO_DB', 'gatewaye_db')
    
    
class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    MONGO_URI = environ.get('TEST_MONGO_URL', 'mongodb://root:password@localhost:27017/test_gatewaye_db?authSource=admin')
    

class ProductionConfig(BaseConfig):
    """Production configuration."""
    MONGO_URI = environ.get('MONGO_URL', 'mongodb://root:password@localhost:27017/gatewaye_db?authSource=admin')
    DB_NAME = environ.get('DB_NAME', 'gatewaye_db')
    

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