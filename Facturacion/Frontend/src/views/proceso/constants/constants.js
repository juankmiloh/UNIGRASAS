/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumnsItems: [{
            label: 'Código',
            prop: 'coditem',
            width: 95
        },
        {
            label: 'Producto',
            prop: 'item',
            width: 270
        },
        {
            label: 'Precio',
            prop: 'precio',
            // width: 125
        },
        {
            label: 'Cantidad',
            prop: 'cantidad',
            width: 110
        },
        {
            label: 'Valor',
            prop: 'total',
            width: 110
        }
    ],
    formTercero: {
        idtercero: '',
        persona: '',
        documento: '',
        nombre: '',
        direccion: '',
        email: ''
    },
    rulesFormTercero: {
        persona: [{
            required: true,
            message: 'Seleccione un tipo de persona',
            trigger: 'change'
        }],
        documento: [
            { required: true, message: 'Ingrese un documento' },
            { type: 'number', message: 'Este campo debe ser numérico' }
        ],
        nombre: [
            { required: true, message: 'Ingrese un nombre', trigger: 'blur' },
        ],
        direccion: [
            { required: true, message: 'Ingrese una dirección', trigger: 'blur' },
        ],
        email: [
            { type: "email", required: true, message: 'Ingrese un correo electrónico válido', trigger: 'blur' },
        ],
    },
    formItem: {
        idfactura: '',
        iditem: '',
        cantidad: '',
        precio: ''
    },
    domItem: [{
            type: 'select',
            prop: 'iditem',
            label: 'Producto',
            placeholder: 'Seleccione un producto'
        },
        {
            type: 'number',
            prop: 'cantidad',
            label: 'Cantidad'
        },
        {
            type: 'number',
            prop: 'precio',
            label: 'Precio'
        },
    ],
    rulesFormItem: {
        iditem: [{
            required: false,
            message: 'Seleccione un producto',
            trigger: 'change'
        }],
        cantidad: [
            { required: true, message: 'Ingrese la cantidad' },
            { type: 'number', message: 'Este campo debe ser numérico' }
        ],
        precio: [
            { required: true, message: 'Ingrese un precio' },
            { type: 'number', message: 'Este campo debe ser numérico' }
        ]
    },
    dataFormItem: {
        iditem: [{
                id: 1,
                label: 'Producto1',
                value: 1
            },
            {
                id: 2,
                label: 'Producto2',
                value: 2
            }
        ]
    }
};