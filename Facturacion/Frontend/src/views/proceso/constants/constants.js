/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumnsItems: [{
            label: 'Código',
            prop: 'coditem',
            width: 100
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
            // width: 230
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
    }
};