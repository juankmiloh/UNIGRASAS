from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class ItemsRepository:
    def __init__(self, db):
        self.db = db

    def get_items_bd(self):
        sql = '''
            SELECT * FROM ITEM;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_items_proceso_bd(self, idProceso):
        sql = '''
            SELECT T.IDTERCEROS, TP.NOMBRE AS PERSONA, T.DOCUMENTO, T.NOMBRE, T.DIRECCION, T.EMAIL FROM TERCEROS T, TIPOPERSONA TP
            WHERE T.IDTIPOPERSONA = TP.IDTIPOPERSONA AND T.IDPROCESO = :IDPROCESO_ARG ORDER BY T.IDTERCEROS DESC;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def items_insert_bd(self, items):
        print('-------------------------------------')
        print('OBJ TERCERO -> ', items)
        print('-------------------------------------')
        sql = '''
            INSERT INTO TERCEROS(IDPROCESO, IDTIPOPERSONA, DOCUMENTO, NOMBRE, DIRECCION, EMAIL)
            VALUES (:IDPROCESO_ARG, :IDTIPOPERSONA_ARG, :DOCUMENTO_ARG, :NOMBRE_ARG, :DIRECCION_ARG, :EMAIL_ARG);
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=items["idproceso"], IDTIPOPERSONA_ARG=items["persona"], DOCUMENTO_ARG=items["documento"], NOMBRE_ARG=items["nombre"], DIRECCION_ARG=items["direccion"], EMAIL_ARG=items["email"])

    def items_update_bd(self, items):
        print('-------------------------------------')
        print('* TERCERO A ACTUALIZAR -> ', items)
        print('-------------------------------------')

        sql = '''
            UPDATE 
                TERCEROS
	        SET 
                IDTIPOPERSONA = :IDTIPOPERSONA_ARG,
                DOCUMENTO = :DOCUMENTO_ARG,
                NOMBRE = :NOMBRE_ARG,
                DIRECCION = :DIRECCION_ARG,
                EMAIL = :EMAIL_ARG
	        WHERE IDTERCEROS = :IDTERCERO_ARG;
        '''
        self.db.engine.execute(text(sql), IDTERCERO_ARG=items["idtercero"], IDTIPOPERSONA_ARG=items["persona"], DOCUMENTO_ARG=items["documento"], NOMBRE_ARG=items["nombre"], DIRECCION_ARG=items["direccion"], EMAIL_ARG=items["email"])
            
                        
    def items_delete_bd(self, idtercero):
        print('-------------------------------------')
        print('* TERCERO A ELIMINAR -> ', idtercero)
        print('-------------------------------------')
        sql = '''
            DELETE FROM TERCEROS
            WHERE IDTERCEROS = :IDTERCERO_ARG;
        '''
        self.db.engine.execute(text(sql), IDTERCERO_ARG=idtercero)