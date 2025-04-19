import re

def normalize_route(path: str) -> str:
    """
    Convierte una ruta con valores concretos (como IDs) a una ruta con parámetros.
    Ej: /api/v1/auth/users/42 → /api/v1/auth/users/<int:id>
    """
    parts = path.rstrip("/").split("/")
    last_item = parts[-1]
    excepted_items = ["login", "logout", "create", "get-user", "house-projects", "sync"]

    if last_item in excepted_items:
        return path
    elif last_item.isdigit():
        parts[-1] = "<int:id>"
    elif re.match(r"^[a-zA-Z0-9_-]+$", last_item): 
        parts[-1] = "<string:param>"

    return "/".join(parts)