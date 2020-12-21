<template>
  <el-row>
    <el-col :md="24">
      <el-card class="box-card div-causas-header">
        <!-- <div slot="header" class="clearfix">
          <span>Card name</span>
          <el-button style="float: right; padding: 3px 0" type="text">Operation button</el-button>
        </div> -->
        <el-table
          ref="multipleTable"
          v-loading="loading"
          :data="listaItems"
          style="width: 100%; border: 1px solid #d8ebff;"
          height="37vh"
          border
          fit
          highlight-current-row
        >
          <el-table-column
            v-for="column in tableColumnsItems"
            :key="column.label"
            :label="column.label"
            :prop="column.prop"
            align="center"
            :width="column.width"
            sortable
          >
            <template slot-scope="scope">
              <div v-if="column.prop === 'item'"><el-tag type="primary">{{ scope.row[column.prop] }}</el-tag></div>
              <div v-else-if="column.prop === 'precio'">$ {{ new Intl.NumberFormat("de-DE").format(scope.row[column.prop]) }}</div>
              <div v-else-if="column.prop === 'total'">$ {{ getTotal(scope.row) }}</div>
              <div v-else>{{ scope.row[column.prop] }}</div>
            </template>
          </el-table-column>
          <el-table-column align="center" width="130">
            <!-- eslint-disable-next-line -->
            <template slot="header" slot-scope="scope">
              <el-button
                style="border: 1px solid #67c23a"
                size="mini"
                icon="el-icon-circle-plus"
                round
                @click="handleAgregar()"
              >Agregar</el-button>
            </template>
            <template slot-scope="scope">
              <el-button
                :disabled="!vendedorEditar"
                size="mini"
                type="success"
                icon="el-icon-edit"
                @click="handleEdit(scope.row)"
              />
              <el-button
                :disabled="!vendedorEditar"
                size="mini"
                type="danger"
                icon="el-icon-delete-solid"
                @click="handleDelete(scope.row)"
              />
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>

    <!-- Modal de confirmacion para agregar / editar un item -->

    <modal-agregar
      :modaltitulo="tituloModalItem"
      :modalvisible="dialogVisibleItem"
      :modalform="formItem"
      :domcomponents="domItem"
      :rulesform="rulesFormItem"
      :datamodal="dataFormItem"
      :action="modalAction"
      @confirmar="submitAgregar"
    />

    <!-- Modal de confirmacion para borrar un item -->

    <modal-delete
      titulo="Advertencia"
      :mensaje="mensajeModalDelete"
      :modalvisible="deleteDialogVisible"
      @confirmar="submitDelete"
    />
  </el-row>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import ModalAgregar from '@/components/ModalAgregar'
import ModalDelete from '@/components/ModalConfirm'
import { CONSTANTS } from '../constants/constants'
import { getListFacturaItems } from '@/api/unigrasas/factura-has-item'

export default {
  directives: { elDragDialog },
  components: {
    ModalAgregar,
    ModalDelete
  },
  props: {
    idproceso: {
      type: String,
      required: true
    },
    editar: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      loading: false,
      tableColumnsItems: CONSTANTS.tableColumnsItems,
      listaItems: [],
      vendedorEditar: this.editar,
      dialogVisibleItem: false,
      deleteDialogVisible: false,
      mensajeModalDelete: '',
      tituloModalItem: '',
      formItem: {},
      domItem: CONSTANTS.domItem,
      rulesFormItem: CONSTANTS.rulesFormItem,
      dataFormItem: CONSTANTS.dataFormItem,
      modalAction: '',
      formModelItem: CONSTANTS.formItem
    }
  },
  watch: {
    editar: {
      deep: true,
      handler(val) {
        console.log('antes !abogadoEditar" -> ', this.editar)
        this.abogadoEditar = val
        console.log('despues !abogadoEditar" -> ', this.editar)
      }
    },
    formModelItem: {
      deep: true,
      handler(val) {
        console.log('Modelo items -> ', val)
        this.formItem = val
      }
    }
  },
  async created() {
    this.getFacturaItems()
  },
  methods: {
    handleAgregar() {
      this.formModelItem.idfactura = this.idproceso
      this.tituloModalItem = 'Agregar item'
      this.modalAction = 'Agregar'
      this.dialogVisibleItem = true
    },
    handleEdit(data) {
      console.log('data -> ', data)
      this.formModelItem = data
      this.tituloModalItem = 'Editar item'
      this.modalAction = 'Editar'
      this.dialogVisibleItem = true
    },
    handleDelete(data) {
      this.mensajeModalDelete = `¿Realmente desea quitar <b>${data.item}</b>?`
      this.deleteDialogVisible = true
    },
    async submitAgregar(confirm) {
      if (confirm) {
        // this.loading = true
        // await deleteCausal(this.causalDel).then(async(response) => {
        //   this.$notify({
        //     title: 'Información',
        //     message: 'Se ha eliminado la causal!',
        //     position: 'bottom-right',
        //     type: 'success',
        //     duration: 2000
        //   })
        //   await this.getCausal(this.idproceso)
        //   this.getCausales()
        //   this.dialogVisibleItem = false
        // })
      } else {
        this.formModelItem = {}
        this.dialogVisibleItem = false
      }
    },
    async submitDelete(confirm) {
      if (confirm) {
        // this.loading = true
        // await deleteCausal(this.causalDel).then(async(response) => {
        //   this.$notify({
        //     title: 'Información',
        //     message: 'Se ha eliminado la causal!',
        //     position: 'bottom-right',
        //     type: 'success',
        //     duration: 2000
        //   })
        //   await this.getCausal(this.idproceso)
        //   this.getCausales()
        //   this.deleteDialogVisible = false
        // })
      } else {
        this.deleteDialogVisible = false
      }
    },
    async getFacturaItems() {
      await getListFacturaItems(this.idproceso).then((response) => {
        console.log('LISTA DE ITEMS -> ', response)
        this.listaItems = response
        let total = 0
        this.listaItems.forEach(element => {
          total = total + element.cantidad * element.precio
        })
        this.$emit('total', total)
      })
    },
    getTotal(data) {
      const total = data.cantidad * data.precio
      return new Intl.NumberFormat('de-DE').format(total)
    }
  }
}
</script>

<style lang="scss" scoped>
</style>

<style>
.div-causas .div-causas-header .el-card__header {
  padding-top: 4%;
  padding-left: 4%;
  height: 7vh;
}
</style>
