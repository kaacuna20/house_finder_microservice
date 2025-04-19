from flask import request, jsonify
import socket

def validate_origin_middleware(app, allow_origins):
    @app.before_request
    def check_origin():

        remote_ip = request.remote_addr
        #hostname = socket.gethostbyaddr(remote_ip)
        #print(f"Origen IP: {remote_ip}, Hostname: {hostname}")
        print("Origen IP:", remote_ip)
        if remote_ip not in allow_origins:
            return jsonify({"msg": "Access denied: IP not allowed", "ip": remote_ip}), 403