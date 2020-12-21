import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
from ..repository import ItemsRepository
from ..util.web_util import format_date
from ..util.web_util import add_wrapper

class ItemsService:

    def get_items(self, items_repository: ItemsRepository):
        items = []
        data = items_repository.get_items_bd()
        for result in data:
            items.append(
                {
                    'value': result[0],
                    'id': result[1],
                    'label': result[2]
                }
            )
        return items

    def get_items_proceso(self, items_repository: ItemsRepository, idproceso):
        items = []
        data = items_repository.get_items_proceso_bd(idproceso)
        for result in data:                
            items.append(
                {
                    'idtercero': result[0],
                    'persona': result[1],
                    'documento': result[2],
                    'nombre': result[3],
                    'direccion': result[4],
                    'email': result[5],
                }
            )
        return items

    def items_insert(self, items_repository: ItemsRepository, items):
        items_repository.items_insert_bd(items)
        return add_wrapper(['items registrada con éxito!'])

    def items_update(self, items_repository: ItemsRepository, dataitems):
        items_repository.items_update_bd(dataitems)
        return add_wrapper(['items actualizada con éxito!'])

    def items_delete(self, items_repository: ItemsRepository, idtercero):
        items_repository.items_delete_bd(idtercero)
        return add_wrapper(['items borrada con éxito!'])