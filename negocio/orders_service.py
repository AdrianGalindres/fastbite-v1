# negocio/orders_service.py
# CAPA DE LOGICA DE NEGOCIO.
# Regla de oro: esta capa SOLO puede llamar a "acceso_datos", NUNCA a "persistencia" directamente.

from acceso_datos import orders_repository, menu_repository


def crear_pedido(usuario: str, items: list):
    """
    Crea un pedido validando reglas de negocio reales:
    - Debe tener al menos 1 producto
    - Cada producto (id) debe existir en el menu
    Lanza ValueError si alguna regla se incumple.
    """
    # TODO 1: valida que la lista "items" no este vacia.
    # Si esta vacia, lanza: raise ValueError("El pedido debe tener al menos 1 producto")

    # TODO 2: para cada item en items, valida que exista en el menu
    # usando menu_repository.obtener_por_id(item["producto_id"])
    # Si no existe, lanza: raise ValueError(f"El producto {item['producto_id']} no existe en el menu")

    # TODO 3: si todas las validaciones pasan, llama a
    # orders_repository.crear(usuario, items) y retorna el resultado
    pass


def listar_pedidos():
    # TODO 4: retorna orders_repository.obtener_todos()
    pass


def obtener_pedido(pedido_id: int):
    # TODO 5: retorna orders_repository.obtener_por_id(pedido_id)
    pass
