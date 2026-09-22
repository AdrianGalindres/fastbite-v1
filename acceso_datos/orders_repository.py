# acceso_datos/orders_repository.py
# CAPA DE ACCESO A DATOS para pedidos. Unica capa autorizada a tocar db.py
# para todo lo relacionado con pedidos.

from persistencia import db


def crear(usuario: str, items: list):
    """Crea un nuevo pedido y lo guarda en la 'base de datos' en memoria."""
    # TODO 1: crea un diccionario "pedido" con:
    #   id -> usa db.siguiente_id_pedido
    #   usuario -> el parametro recibido
    #   items -> el parametro recibido
    #   estado -> "creado"
    # TODO 2: agrega el pedido a db.pedidos
    # TODO 3: incrementa db.siguiente_id_pedido en 1
    # TODO 4: retorna el pedido creado
    pass


def obtener_todos():
    """Devuelve todos los pedidos guardados."""
    # TODO 5: retorna db.pedidos
    pass


def obtener_por_id(pedido_id: int):
    """Busca un pedido por su id. Devuelve None si no existe."""
    # TODO 6: recorre db.pedidos y devuelve el que coincida con pedido_id
    pass
