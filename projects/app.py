# app.py
from flask import Flask
from src import models
from src.database.db_conection import db, migrate
from src.routes.project import project_bp
from src.routes.municipality import municipality_bp
from src.routes.company import company_bp
from src.routes.project_user import project_user_bp
from src.utils.settings import Settings
from src.utils.middleware import validate_origin_middleware
from logging.config import dictConfig

settings_module = Settings.get_config()
dictConfig(settings_module.LOGGING_CONFIG)

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(settings_module)
print(app.config)
    
db.init_app(app)
migrate.init_app(app, db)
root_route = app.config['URL_PREFIX']
    
allow_origins = app.config['ALLOW_ORIGIN']

validate_origin_middleware(app, allow_origins=allow_origins)

# Register blueprints
app.register_blueprint(project_bp, url_prefix=root_route)
app.register_blueprint(municipality_bp, url_prefix=f"{root_route}/municipality")
app.register_blueprint(company_bp, url_prefix=f"{root_route}/company")
app.register_blueprint(project_user_bp, url_prefix=f"{root_route}/project_user")


if __name__ == "__main__":
    app.run(debug=settings_module.DEBUG, host="0.0.0.0", port=5001)