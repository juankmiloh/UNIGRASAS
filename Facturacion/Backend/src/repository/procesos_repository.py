from sqlalchemy.sql import text


class ProcesosRepository:
    def __init__(self, db):
        self.db = db

    def get_procesos_bd(self):
        sql = '''
            SELECT F.IDFACTURA, C.NOMBRE, F.F_EMISION, F.TOTAL, U.IDUSUARIO, CONCAT_WS(' ', U.NOMBRE, U.APELLIDO) AS USUARIO FROM FACTURA F, CLIENTE C, USUARIO U
            WHERE F.IDCLIENTE = C.IDCLIENTE
            AND F.IDUSUARIO = U.IDUSUARIO
            ORDER BY F.IDFACTURA DESC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_proceso_inicial_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT * FROM
            (
                SELECT 
                    P.IDPROCESO,
                    P.RADICADOPROCESO AS EXPEDIENTE,
                    P.FECHACADUCIDAD AS CADUCIDAD,
                    EMP.NOMBRE AS EMPRESA,
                    ES.NOMBREESTADO AS ESTADO,
                    E.NOMBRE AS ACTUALETAPA,
                    (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=E.SIGUIENTEETAPA) AS PROXETAPA,
                    S.NOMBRE AS SERVICIO,
                    U.IDUSUARIO AS IDUSUARIO,
                    U.NOMBRE || ' ' || U.APELLIDO AS USUARIO,
                    EP.ETAPA
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
                    AND P.IDPROCESO = :IDPROCESO_ARG
            ) PROCESO,
            (
                SELECT 
                    P.IDPROCESO,
                    MIN(EP.ETAPA) AS IDETAPA
                FROM PROCESO P, ETAPA_PROCESO EP
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND P.IDPROCESO = :IDPROCESO_ARG
                GROUP BY P.IDPROCESO
            ) ETAPA
            WHERE
                PROCESO.IDPROCESO = ETAPA.IDPROCESO
                AND PROCESO.ETAPA = ETAPA.IDETAPA;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()
    
    def get_proceso_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT * FROM
            (
                SELECT 
                    P.IDPROCESO,
                    P.RADICADOPROCESO AS EXPEDIENTE,
                    P.FECHACADUCIDAD AS CADUCIDAD,
                    EMP.NOMBRE AS EMPRESA,
                    PC.NOMCAUSAL,
                    P.FECHAHECHOS,
                    P.DESCRIPCION,
                    ES.NOMBREESTADO AS ESTADO,
                    E.NOMBRE AS ACTUALETAPA,
                    (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=E.SIGUIENTEETAPA) AS PROXETAPA,
                    DR.TIPODESCISIONRECURSO AS DECISION,
                    TS.NOMBRETIPOSANCION AS TIPOSANCION,
                    P.MONTOSANCION,
                    S.NOMBRE AS SERVICIO,
                    U.IDUSUARIO AS IDUSUARIO,
                    EP.ETAPA
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES, PROCESO_CAUSAL PC, TIPOSANCION TS, DESCISIONRECURSO DR
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.IDPROCESO = PC.IDPROCESO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
                    AND P.TIPOSANCION = TS.IDTIPOSANCION
                    AND P.DESCISIONRECURSO = DR.IDDESCISIONRECURSO
                    AND P.IDPROCESO = :IDPROCESO_ARG
            ) PROCESO,
            (
                SELECT 
                    P.IDPROCESO,
                    MIN(EP.ETAPA) AS IDETAPA
                FROM PROCESO P, ETAPA_PROCESO EP
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND P.IDPROCESO = :IDPROCESO_ARG
                GROUP BY P.IDPROCESO
            ) ETAPA
            WHERE
                PROCESO.IDPROCESO = ETAPA.IDPROCESO
                AND PROCESO.ETAPA = ETAPA.IDETAPA;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def proceso_insert_bd(self, proceso):
        print('-------------------------------------')
        print('OBJ FACTURA -> ', proceso)
        print('-------------------------------------')
        sql = '''
            INSERT INTO FACTURA(IDCLIENTE, IDUSUARIO, IDESTADO, DIVISA, F_EMISION, TOTAL, F_REGISTRO)
            VALUES (:IDCLIENTE_ARG, :IDUSUARIO_ARG, :ESTADO_ARG, :DIVISA_ARG, STR_TO_DATE(:F_EMISION_ARG,'%d/%m/%Y %H:%i:%s'), :TOTAL_ARG, CURRENT_TIMESTAMP);
        '''
        resultsql = self.db.engine.execute(text(sql), IDCLIENTE_ARG=proceso["cliente"], IDUSUARIO_ARG=proceso["usuario"], ESTADO_ARG=1, DIVISA_ARG=proceso["divisa"], TOTAL_ARG=0, F_EMISION_ARG=proceso["f_emision"])

        return resultsql
    
    def proceso_usuario_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* FACTURA A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE FACTURA
            SET IDUSUARIO = :IDUSUARIO_ARG
            WHERE IDFACTURA = :IDFACTURA_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDFACTURA_ARG=dataProceso["idfactura"], IDUSUARIO_ARG=dataProceso["usuario"])

        return resultsql

    def proceso_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* PROCESO A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')

        if dataProceso["caducidad"] == 'None':
            dataProceso["caducidad"] = None

        sql = '''
            UPDATE 
                PROCESO
	        SET 
                RADICADOPROCESO = :RADICADO_ARG,
                USUARIOASIGNADO = :USUARIO_ARG,
                EMPRESA = :EMPRESA_ARG,
                IDSERVICIO = :SERVICIO_ARG,
                TIPOSANCION = :TIPOSANCION_ARG, 
                DESCISIONRECURSO = :DECISION_ARG,
                MONTOSANCION = :SANCION_ARG,
                FECHAHECHOS = :FECHAHECHOS_ARG,
                DESCRIPCION = :DESCRIPCION_ARG,
                FECHACADUCIDAD = :CADUCIDAD_ARG
	        WHERE
                IDPROCESO = :IDPROCESO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=dataProceso["idproceso"], RADICADO_ARG=dataProceso["expediente"], USUARIO_ARG=dataProceso["usuario"], EMPRESA_ARG=dataProceso["empresa"], SERVICIO_ARG=dataProceso["servicio"], TIPOSANCION_ARG=dataProceso["tipo_sancion"], DECISION_ARG=dataProceso["decision"], SANCION_ARG=dataProceso["sancion"], FECHAHECHOS_ARG=dataProceso["fecha_hechos"], DESCRIPCION_ARG=dataProceso["descripcion"], CADUCIDAD_ARG=dataProceso["caducidad"])

        # for result in dataProceso["causa"]:
        print('----------DATA CAUSA---------------', dataProceso["causa"])

        sql = '''
            UPDATE 
                PROCESO_CAUSAL
            SET
                NOMCAUSAL = :CAUSAL_ARG
            WHERE
                IDPROCESO = :IDPROCESO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=dataProceso["idproceso"], CAUSAL_ARG=dataProceso["causa"])
    
    def proceso_delete_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO A ELIMINAR -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE PROCESO
            SET FASE = 3
            WHERE IDPROCESO = :IDPROCESO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso)