from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class FacturaHasItemRepository:
    def __init__(self, db):
        self.db = db

    def get_facturaHasItem_bd(self):
        sql = '''
            SELECT * FROM FACTURA_HAS_ITEM;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_facturaHasItem_proceso_bd(self, idProceso):
        print('---------- IDFACTURA ', idProceso, ' ----------------')
        sql = '''
            SELECT FHI.*, I.COD_ITEM, I.NOMBRE, I.DESCRIPCION FROM FACTURA_HAS_ITEM FHI, ITEM I
            WHERE 
            FHI.IDFACTURA = :IDPROCESO_ARG
            AND FHI.IDITEM = I.IDITEM;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def facturaHasItem_insert_bd(self, facturaHasItem):
        print('-------------------------------------')
        print('OBJ ETAPA -> ', facturaHasItem)
        print('-------------------------------------')
        sql = '''
            INSERT INTO ETAPA_PROCESO(ETAPA, PROCESO, FECHAINICIOETAPA, FECHAFINETAPA, RADICADOETAPA, OBSERVACIONETAPA)
            VALUES (:ETAPA_ARG, :IDPROCESO_ARG, :FECHAINICIO_ARG, :FECHAFIN_ARG, :RADICADO_ARG, :OBSERVACION_ARG);
        '''
        self.db.engine.execute(text(sql), ETAPA_ARG=facturaHasItem["facturaHasItem"], IDPROCESO_ARG=facturaHasItem["idproceso"], FECHAINICIO_ARG=facturaHasItem["fechaInicioFacturaHasItem"], FECHAFIN_ARG=facturaHasItem["fechaFinFacturaHasItem"], RADICADO_ARG=facturaHasItem["radicadoFacturaHasItem"], OBSERVACION_ARG=facturaHasItem["observacionFacturaHasItem"])

        self.update_fase_proceso(facturaHasItem["idproceso"])

    def facturaHasItem_update_bd(self, facturaHasItem):
        print('-------------------------------------')
        print('* ETAPA A ACTUALIZAR -> ', facturaHasItem)
        print('-------------------------------------')

        if facturaHasItem["fechaFinFacturaHasItem"] == 'Invalid date':
            facturaHasItem["fechaFinFacturaHasItem"] = None

        sql = '''
            UPDATE 
                ETAPA_PROCESO
	        SET 
                FECHAINICIOETAPA= :FECHAINICIO_ARG,
                FECHAFINETAPA = :FECHAFIN_ARG,
                RADICADOETAPA = :RADICADO_ARG,
                OBSERVACIONETAPA = :OBSERVACION_ARG
	        WHERE RADICADOETAPA = :RADICADO_ARG;
        '''
        self.db.engine.execute(text(sql), FECHAINICIO_ARG=facturaHasItem["fechaInicioFacturaHasItem"], FECHAFIN_ARG=facturaHasItem["fechaFinFacturaHasItem"], RADICADO_ARG=facturaHasItem["radicadoFacturaHasItem"], OBSERVACION_ARG=facturaHasItem["observacionFacturaHasItem"])

        self.update_fase_proceso(facturaHasItem["idproceso"])
            
                        
    def facturaHasItem_delete_bd(self, facturaHasItem):
        print('-------------------------------------')
        print('* ETAPA A ELIMINAR -> ', facturaHasItem)
        print('-------------------------------------')
        sql = '''
            DELETE FROM ETAPA_PROCESO
            WHERE RADICADOETAPA = :RADICADO_ARG;
        '''
        self.db.engine.execute(text(sql), RADICADO_ARG=facturaHasItem["radicadoFacturaHasItem"])

        self.update_fase_proceso(facturaHasItem["idproceso"])

    def update_fase_proceso(self, idproceso):
        sql = '''
            SELECT E.NOMBRE FROM ETAPA_PROCESO EP, ETAPA E WHERE PROCESO=:IDPROCESO_ARG AND EP.ETAPA=E.IDETAPA;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=idproceso).fetchall()

        countFacturaHasItems = 0
        terminado = False
        fase = 0
        
        for result in resultsql:
            facturaHasItem = result[0]
            if facturaHasItem != 'Memorando de devolución':
                if facturaHasItem != 'Memorando de alcance':
                    print('------------ ETAPA ----', facturaHasItem, '----------------')
                    countFacturaHasItems = countFacturaHasItems + 1
                    if facturaHasItem == 'Archivo':
                        terminado = True

        print('------------ CANTIDAD ETAPAS ----', countFacturaHasItems, '----------------')
        print('------------ TERMINADO ----', terminado, '----------------')

        if countFacturaHasItems >= 13 and terminado:
            print('------------ PROCESO TERMINADO ----------------')
            fase = 2 # Proceso terminado
        else:
            fase = 1 # Proceso En curso

        sql = '''
                UPDATE PROCESO SET FASE=:FASE_ARG WHERE IDPROCESO=:IDPROCESO_ARG;
            '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=idproceso, FASE_ARG=fase)