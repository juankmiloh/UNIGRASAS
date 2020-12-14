from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class ClientesRepository:
    def __init__(self, db):
        self.db = db

    def get_clientes_bd(self):
        sql = '''
            SELECT * FROM CLIENTE;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_clientes_proceso_bd(self, idProceso):
        sql = '''
            SELECT T.IDTERCEROS, TP.NOMBRE AS PERSONA, T.DOCUMENTO, T.NOMBRE, T.DIRECCION, T.EMAIL FROM TERCEROS T, TIPOPERSONA TP
            WHERE T.IDTIPOPERSONA = TP.IDTIPOPERSONA AND T.IDPROCESO = :IDPROCESO_ARG ORDER BY T.IDTERCEROS DESC;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def clientes_insert_bd(self, clientes):
        print('-------------------------------------')
        print('OBJ TERCERO -> ', clientes)
        print('-------------------------------------')
        sql = '''
            INSERT INTO TERCEROS(IDPROCESO, IDTIPOPERSONA, DOCUMENTO, NOMBRE, DIRECCION, EMAIL)
            VALUES (:IDPROCESO_ARG, :IDTIPOPERSONA_ARG, :DOCUMENTO_ARG, :NOMBRE_ARG, :DIRECCION_ARG, :EMAIL_ARG);
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=clientes["idproceso"], IDTIPOPERSONA_ARG=clientes["persona"], DOCUMENTO_ARG=clientes["documento"], NOMBRE_ARG=clientes["nombre"], DIRECCION_ARG=clientes["direccion"], EMAIL_ARG=clientes["email"])

    def clientes_update_bd(self, clientes):
        print('-------------------------------------')
        print('* TERCERO A ACTUALIZAR -> ', clientes)
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
        self.db.engine.execute(text(sql), IDTERCERO_ARG=clientes["idtercero"], IDTIPOPERSONA_ARG=clientes["persona"], DOCUMENTO_ARG=clientes["documento"], NOMBRE_ARG=clientes["nombre"], DIRECCION_ARG=clientes["direccion"], EMAIL_ARG=clientes["email"])
            
                        
    def clientes_delete_bd(self, idtercero):
        print('-------------------------------------')
        print('* TERCERO A ELIMINAR -> ', idtercero)
        print('-------------------------------------')
        sql = '''
            DELETE FROM TERCEROS
            WHERE IDTERCEROS = :IDTERCERO_ARG;
        '''
        self.db.engine.execute(text(sql), IDTERCERO_ARG=idtercero)