/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumnsAdmin: [{
            label: 'Numeración',
            prop: 'idfactura',
            width: '',
            filter: 'filterFactura'
        },
        {
            label: 'Cliente / CUFE',
            prop: 'cliente',
            width: 350,
            filter: 'filterCliente'
        },
        {
            label: 'Creacion',
            prop: 'f_creacion',
            width: '',
            filter: 'filterFcreacion'
        },
        {
            label: 'Total',
            prop: 'total',
            width: '',
            filter: 'filterTotal'
        },
        {
            label: 'Vendedor',
            prop: 'usuario',
            width: '',
            filter: 'filterVendedor'
        }
    ],
    tableColumnsAbogado: [
        // {
        //     label: '#',
        //     prop: 'idproceso',
        //     width: 70
        // },
        {
            label: 'Expediente',
            prop: 'expediente',
            filter: 'filterExpediente'
        },
        {
            label: 'Servicio',
            prop: 'servicio',
            filter: 'filterServicio'
        },
        {
            label: 'Empresa',
            prop: 'empresa',
            width: 270,
            filter: 'filterEmpresa'
        },
        {
            label: 'Caducidad',
            prop: 'caducidad',
            filter: 'filterCaducidad'
        },
        {
            label: 'Estado',
            prop: 'estado',
            width: 210,
            filter: 'filterEstado'
        },
    ],
    tableColumnsEtapas: [{
            label: '#',
            prop: 'idetapa',
            width: 70
        },
        {
            label: 'Radicado',
            prop: 'radicadoEtapa'
        },
        {
            label: 'Etapa',
            prop: 'nombreEtapa',
            width: 300
        },
        {
            label: 'Fecha de inicio',
            prop: 'fechaInicioEtapa'
        },
        {
            label: 'Fecha fin',
            prop: 'fechaFinEtapa'
        },
        {
            label: 'Observación',
            prop: 'observacionEtapa',
            width: 300
        }
    ],
    filter: [
        { text: 'Energía', value: 'Energía' },
        { text: 'Gas', value: 'Gas' },
        { text: 'GLP', value: 'GLP' },
    ],
    rulesFormProceso: {
        // idfactura: [
        //     { required: true, message: 'Ingrese numeración', trigger: 'blur' },
        //     // { min: 17, max: 17, message: 'La longitud del expediente debe ser de 17 caracteres', trigger: 'blur' }
        // ],
        cliente: [{
            required: true,
            message: 'Seleccione un cliente',
            trigger: 'change'
        }],
        divisa: [{
            required: true,
            message: 'Seleccione una divisa',
            trigger: 'change'
        }],
        f_emision: [{
            type: 'date',
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        usuario: [{
            required: true,
            message: 'Seleccione un usuario',
            trigger: 'change'
        }],
    },
    formAgregar: {
        // idfactura: '',
        cliente: '',
        divisa: '',
        f_emision: '',
        usuario: ''
    },
    formUsuario: {
        usuario: '',
        idfactura: ''
    },
    formDetalleProceso: {
        expediente: '',
        tipo_sancion: '',
        decision: '',
        sancion: '',
        causa: [],
        descripcion: ''
    },
    rulesDetalleProceso: {
        expediente: [
            { required: true, message: 'Ingrese un expediente', trigger: 'blur' },
            { min: 17, max: 17, message: 'La longitud debe ser de 17 caracteres', trigger: 'blur' }
        ],
        empresa: [{
            required: true,
            message: 'Seleccione una empresa',
            trigger: 'change'
        }],
        tipo_sancion: [{
            required: false,
            message: 'Seleccione un tipo de sanción',
            trigger: 'change'
        }],
        sancion: [
            { required: false, message: 'Valor sanción requerido' },
            { type: 'number', message: 'La sanción debe ser un número' }
        ],
        decision: [{
            required: false,
            message: 'Seleccione una decision',
            trigger: 'change'
        }],
        causa: [{
            required: true,
            message: 'Seleccione una causal',
            trigger: 'change'
        }],
        fecha_hechos: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        caducidad: [{
            required: false,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }]
    },
    formAgregarEtapa: {
        etapa: '',
        fechaInicioEtapa: null,
        fechaFinEtapa: null,
        observacionEtapa: ''
    },
    rulesFormEtapa: {
        etapa: [{
            required: true,
            message: 'Seleccione una etapa',
            trigger: 'change'
        }],
        fechaInicioEtapa: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        observacionEtapa: [{
            required: false,
            message: 'Ingrese una observación',
            trigger: 'blur'
        }]
    },
    formUser: {
        nombre: '',
        apellido: '',
        genero: '',
        nickname: '',
        contrasena: '',
        rol: '',
        descripcion: '',
        avatar: '',
        token: ''
    },
    rulesFormUser: {
        nombre: [
            { required: true, message: 'Ingrese nombre', trigger: 'blur' }
        ],
        apellido: [
            { required: true, message: 'Ingrese apellido', trigger: 'blur' }
        ],
        genero: [{
            required: true,
            message: 'Seleccione un género',
            trigger: 'change'
        }],
        rol: [{
            required: true,
            message: 'Seleccione un rol',
            trigger: 'change'
        }],
        descripcion: [{
            required: true,
            message: 'Ingrese una descripción del usuario',
            trigger: 'change'
        }],
    },
    dataGenero: [{
            idgenero: 1,
            nombre: 'Hombre'
        },
        {
            idgenero: 2,
            nombre: 'Mujer'
        }
    ]
};