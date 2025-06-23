from flask import Flask
from src.utils.settings import Settings
from src.utils.middleware import validate_origin_middleware
from src.routes.sync import sync_bp
from logging.config import dictConfig

settings_module = Settings.get_config()
dictConfig(settings_module.LOGGING_CONFIG)


app = Flask(__name__)
app.config.from_object(settings_module)

root_route = app.config['URL_PREFIX']
    
allow_origins = app.config['ALLOW_ORIGIN']
validate_origin_middleware(app, allow_origins=allow_origins)

app.register_blueprint(sync_bp, url_prefix=f"{root_route}/sync")


if __name__ == "__main__":
    app.run(debug=settings_module.DEBUG, host="0.0.0.0", port=5002)