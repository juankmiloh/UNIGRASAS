import json

from flask import request

from ..controller import controller
from ..service import ItemsService
from ..repository import ItemsRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'items', methods=['GET'])
def items(items_service: ItemsService, items_repository: ItemsRepository):
    return json.dumps(items_service.get_items(items_repository))

# Obtener detalle de los items de un proceso
@controller.route(API_ROOT_PATH + 'items_proceso', methods=['GET'])
def getItemsProceso(items_service: ItemsService, items_repository: ItemsRepository):
    # Id proceso
    idProceso = request.args.get('idProceso', default='', type=str)
    return json.dumps(items_service.get_items_proceso(items_repository, idProceso))

# Crear un item
@controller.route(API_ROOT_PATH + 'items', methods=['POST'])
def createItems(items_service: ItemsService, items_repository: ItemsRepository):
    items = request.json
    return json.dumps(items_service.items_insert(items_repository, items))

# Actualizar item
@controller.route(API_ROOT_PATH + 'items', methods=['PUT'])
def updateItems(items_service: ItemsService, items_repository: ItemsRepository):
    # Datos items
    dataitems = request.json
    return json.dumps(items_service.items_update(items_repository, dataitems))

# Eliminar un item
@controller.route(API_ROOT_PATH + 'items', methods=['DELETE'])
def deleteItems(items_service: ItemsService, items_repository: ItemsRepository):
    # ID item
    iditem = request.args.get('iditem', default='', type=str)
    return json.dumps(items_service.items_delete(items_repository, iditem))