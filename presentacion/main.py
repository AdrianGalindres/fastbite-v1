# presentacion/main.py
# CAPA DE PRESENTACION.
# Regla de oro: esta capa SOLO puede llamar a "negocio" (Service),
# NUNCA a "acceso_datos" ni a "persistencia" directamente.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from negocio import orders_service
from acceso_datos import menu_repository

app = FastAPI(title="FastBite v1 - Monolito en capas")


class ItemPedido(BaseModel):
    producto_id: int
    cantidad: int


class NuevoPedido(BaseModel):
    usuario: str
    items: list[ItemPedido]


@app.get("/menu")
def ver_menu():
    # TODO 1: retorna menu_repository.obtener_todos()
    pass


@app.post("/pedidos")
def crear_pedido(pedido: NuevoPedido):
    # TODO 2: llama a orders_service.crear_pedido(pedido.usuario, [item.dict() for item in pedido.items])
    # Si lanza ValueError, debes capturarlo y convertirlo en:
    # raise HTTPException(status_code=400, detail=str(error))
    pass


@app.get("/pedidos")
def listar_pedidos():
    # TODO 3: retorna orders_service.listar_pedidos()
    pass


@app.get("/pedidos/{pedido_id}")
def ver_pedido(pedido_id: int):
    # TODO 4: llama a orders_service.obtener_pedido(pedido_id)
    # Si el resultado es None, lanza: raise HTTPException(status_code=404, detail="Pedido no encontrado")
    pass

# TODO 5 (actividad para el hogar): agrega aqui el endpoint
# PUT /pedidos/{pedido_id}/cancelar respetando las 4 capas
