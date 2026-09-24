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
    pass


@app.get("/pedidos")
def listar_pedidos():
    pass


@app.get("/pedidos/{pedido_id}")
def ver_pedido(pedido_id: int):
    pass

# PUT /pedidos/{pedido_id}/cancelar respetando las 4 capas
