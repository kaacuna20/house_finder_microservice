from flask import jsonify

def http_response(status_code, message, data=None, error=None):
    if data is None:
        data = {}
            
    return jsonify({
            "status_code": status_code,
            "message": message,
            "data": data,
            "error": error
        }), status_code