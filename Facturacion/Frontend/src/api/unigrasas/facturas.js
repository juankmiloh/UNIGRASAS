/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListFacturas() {
    return request({
        url: '/procesos',
        method: 'get'
    });
}

export function getProceso(id) {
    return request({
        url: '/proceso/detalle',
        method: 'get',
        params: { 'idProceso': id }
    });
}

export function getProcesoInicial(id) {
    return request({
        url: '/proceso/detalle/inicial',
        method: 'get',
        params: { 'idProceso': id }
    });
}

export function createFactura(data) {
    return request({
        url: '/procesos',
        method: 'post',
        data
    });
}

export function updateFacturaUsuario(data) {
    return request({
        url: '/procesos/usuarioupdate',
        method: 'put',
        data: data
    });
}

export function updateProceso(data) {
    return request({
        url: '/procesos/update',
        method: 'put',
        data: data
    });
}

export function deleteFactura(id) {
    return request({
        url: '/procesos',
        method: 'delete',
        params: { 'idProceso': id }
    });
}