# app.py
#from flask_cors import CORS
from flask import Flask
from flask_jwt_extended import JWTManager
from src import models
from src.database.db_conection import db, migrate
from src.routes.user import user_bp
from src.routes.roles import role_bp
from src.routes.permission import permission_bp
from src.routes.authenticate import auth_bp
from src.utils.settings import Settings
from src.utils.middleware import validate_origin_middleware

settings_module = Settings.get_config()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(settings_module)
print(app.config)

#CORS(app, resources={r"/*": {"origins": settings_module.GATEWEAY_URL}})
    
db.init_app(app)
migrate.init_app(app, db)
root_route = app.config['URL_PREFIX']
    
jwt = JWTManager(app)
jwt.init_app(app)

allow_origins = app.config['ALLOW_ORIGIN']

validate_origin_middleware(app, allow_origins=allow_origins)

# Register blueprints
app.register_blueprint(user_bp, url_prefix=f'{root_route}/users')
app.register_blueprint(role_bp, url_prefix=f'{root_route}/roles')
app.register_blueprint(permission_bp, url_prefix=f'{root_route}/permissions')
app.register_blueprint(auth_bp, url_prefix=f'{root_route}')


if __name__ == "__main__":
    app.run(debug=settings_module.DEBUG, host="0.0.0.0", port=5003)













































#Base.metadata.create_all(bind=engine)
# @app.post("/register")
# def register():
#     data = request.json
#     
#     user = User(username=data["username"], email=data["email"])
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return jsonify({"msg": "User created", "user_id": user.id})

# @app.post("/generate-apikey")
# def generate_key():
#     user_id = request.json.get("user_id")
#     db = SessionLocal()
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     raw_key, hashed_key = generate_api_key()
#     user.api_key = hashed_key
#     db.commit()
#     return jsonify({"api_key": raw_key})  # Show only once

# @app.post("/verify-apikey")
# def verify_key():
#     auth_header = request.headers.get("Authorization")
#     if not auth_header or not auth_header.startswith("ApiKey "):
#         return jsonify({"msg": "Invalid header"}), 401

#     key = auth_header.split(" ")[1]
#     hashed_key = hashlib.sha256(key.encode()).hexdigest()

#     db = SessionLocal()
#     user = db.query(User).filter(User.api_key == hashed_key).first()
#     if not user:
#         return jsonify({"msg": "Invalid API key"}), 403

#     return jsonify({"msg": "API key valid", "username": user.username})

