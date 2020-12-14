import json

from flask import request

from ..controller import controller
from ..service import ClientesService
from ..repository import ClientesRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'clientes', methods=['GET'])
def clientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    return json.dumps(clientes_service.get_clientes(clientes_repository))

# Obtener detalle de los clientes de un proceso
@controller.route(API_ROOT_PATH + 'clientes_proceso', methods=['GET'])
def getClientesProceso(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    # Id proceso
    idProceso = request.args.get('idProceso', default='', type=str)
    return json.dumps(clientes_service.get_clientes_proceso(clientes_repository, idProceso))

# Crear un cliente
@controller.route(API_ROOT_PATH + 'clientes', methods=['POST'])
def createClientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    clientes = request.json
    return json.dumps(clientes_service.clientes_insert(clientes_repository, clientes))

# Actualizar cliente
@controller.route(API_ROOT_PATH + 'clientes', methods=['PUT'])
def updateClientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    # Datos clientes
    dataclientes = request.json
    return json.dumps(clientes_service.clientes_update(clientes_repository, dataclientes))

# Eliminar un cliente
@controller.route(API_ROOT_PATH + 'clientes', methods=['DELETE'])
def deleteClientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    # ID cliente
    idcliente = request.args.get('idcliente', default='', type=str)
    return json.dumps(clientes_service.clientes_delete(clientes_repository, idcliente))