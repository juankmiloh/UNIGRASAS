/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumnsItems: [{
            label: 'Nombre',
            prop: 'nombre',
            width: 300
        },
        {
            label: 'Nit',
            prop: 'nit',
            // width: 270
        },
        {
            label: 'Email',
            prop: 'email',
            // width: 125
        },
        {
            label: 'Teléfono',
            prop: 'telefono',
            // width: 110
        },
        {
            label: 'Fecha registro',
            prop: 'registro',
            // width: 110
        }
    ],
    formItem: {
        idcliente: '',
        tipopersona: '',
        nit: '',
        nombre: '',
        email: '',
        telefono: ''
    },
    domItem: [{
            type: 'radiogroup',
            prop: 'tipopersona',
            label: ' '
        },
        {
            type: 'number',
            prop: 'nit',
            label: 'Nit'
        },
        {
            type: 'text',
            prop: 'nombre',
            label: 'Nombre',
            placeholder: 'Nombre del cliente'
        },
        {
            type: 'text',
            prop: 'email',
            label: 'Email'
        },
        {
            type: 'number',
            prop: 'telefono',
            label: 'Teléfono'
        },
    ],
    rulesFormItem: {
        tipopersona: [{
            required: true,
            message: 'Seleccione un tipo de persona',
            trigger: 'change'
        }],
        nombre: [
            { required: true, message: 'Ingrese un nombre', trigger: 'blur' }
        ],
        nit: [
            { required: true, message: 'Ingrese el NIT' },
            { type: 'number', message: 'Este campo debe ser numérico' }
        ],
        email: [
            { type: "email", required: true, message: 'Ingrese un correo electrónico válido', trigger: 'blur' },
        ],
        telefono: [
            { required: true, message: 'Ingrese número de teléfono' },
            { type: 'number', message: 'Este campo debe ser numérico' }
        ],
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
        ],
        tipopersona: [{
                id: 1,
                label: 'Persona natural',
                value: 1
            },
            {
                id: 2,
                label: 'Persona jurídica',
                value: 2
            }
        ],

    }
};