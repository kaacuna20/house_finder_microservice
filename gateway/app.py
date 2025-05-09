# app.py
from flask import Flask
from src.routes.activity_log import log_bp
from src.routes.routes import route_bp
from src.routes.gateway import gateway_bp
from src.utils.settings import Settings

config = Settings.get_config()

app = Flask(__name__)
app.config.from_object(config)
print(app.config)
root_url = app.config["URL_PREFIX"]

app.register_blueprint(log_bp, url_prefix=f"{root_url}/activity-log")
app.register_blueprint(route_bp, url_prefix=f"{root_url}/routes-table")
app.register_blueprint(gateway_bp, url_prefix=root_url)


if __name__ == "__main__":
    app.run(debug=config.DEBUG, host="0.0.0.0", port=5000)