import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
from ..repository import ClientesRepository
from ..util.web_util import format_date
from ..util.web_util import add_wrapper

class ClientesService:

    def get_clientes(self, clientes_repository: ClientesRepository):
        clientes = []
        data = clientes_repository.get_clientes_bd()
        for result in data:
            clientes.append(
                {
                    'idcliente': result[0],
                    'nombre': result[3]
                }
            )
        return clientes

    def get_clientes_proceso(self, clientes_repository: ClientesRepository, idproceso):
        clientes = []
        data = clientes_repository.get_clientes_proceso_bd(idproceso)
        for result in data:                
            clientes.append(
                {
                    'idtercero': result[0],
                    'persona': result[1],
                    'documento': result[2],
                    'nombre': result[3],
                    'direccion': result[4],
                    'email': result[5],
                }
            )
        return clientess

    def clientes_insert(self, clientes_repository: ClientesRepository, clientes):
        clientes_repository.clientes_insert_bd(clientes)
        return add_wrapper(['clientes registrada con éxito!'])

    def clientes_update(self, clientes_repository: ClientesRepository, dataclientes):
        clientes_repository.clientes_update_bd(dataclientes)
        return add_wrapper(['clientes actualizada con éxito!'])

    def clientes_delete(self, clientes_repository: ClientesRepository, idtercero):
        clientes_repository.clientes_delete_bd(idtercero)
        return add_wrapper(['clientes borrada con éxito!'])