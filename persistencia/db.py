# persistencia/db.py
# Esta capa simula una base de datos usando estructuras en memoria.
# En un proyecto real esto seria PostgreSQL, MySQL, etc.

# TODO 1: crea una lista de diccionarios llamada "menu" con al menos 3 productos.
# Cada producto debe tener: id (int), nombre (str), precio (float)
# Ejemplo de un producto: {"id": 1, "nombre": "Hamburguesa", "precio": 15000}
menu = [
    # TODO: completa aqui los productos del menu
]

# TODO 2: crea una lista vacia llamada "pedidos" donde se iran guardando los pedidos creados
pedidos = []

# TODO 3: crea una variable "siguiente_id_pedido" inicializada en 1,
# que se ira incrementando cada vez que se cree un nuevo pedido
siguiente_id_pedido = 1
