import os
from os import environ, makedirs
from datetime import datetime

log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, f'{datetime.now().strftime("%Y%m%d")}.log')

class BaseConfig:
    SECRET_KEY = environ.get('SECRET_APP_KEY', 'your_secret_key')
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = environ.get('JWT_EXPIRATION_TIME', 3600)  # 1 hour
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HASH_METHOD = environ.get('HASH_METHOD', 'pbkdf2:sha256')
    HASH_SALT_LENGTH = environ.get('HASH_SALT_LENGTH', 16)
    URL_PREFIX = '/api/v1/auth'
    ALLOW_ORIGIN = {"127.0.0.1", environ.get('GATEWAY_IP_1'), environ.get('GATEWAY_IP_2'), environ.get('GATEWAY_IP_3')}
    DEBUG = environ.get('DEBUG', True)
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
    SQLALCHEMY_DATABASE_URI = environ.get('AUTH_DB_URL', 'sqlite:///auth_dev.db')
    
    
class TestingConfig(BaseConfig):
    """Testing configuration."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids overhead
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_AUTH_DB_URL', 'sqlite:///auth_test.db')
    

class ProductionConfig(BaseConfig):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = environ.get('AUTH_DB_URL', 'sqlite:///auth_prod.db')
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
