# acceso_datos/menu_repository.py
# Esta es la CAPA DE ACCESO A DATOS. Es la UNICA capa que puede importar
# y tocar directamente "persistencia/db.py". Nadie mas debe importar db.py.

from persistencia import db


def obtener_todos():
    """Devuelve la lista completa del menu."""
    # TODO 1: retorna db.menu
    pass


def obtener_por_id(producto_id: int):
    """Busca un producto del menu por su id. Devuelve None si no existe."""
    # TODO 2: recorre db.menu y devuelve el producto cuyo "id" coincida con producto_id
    # Si no lo encuentra, debe devolver None
    pass
