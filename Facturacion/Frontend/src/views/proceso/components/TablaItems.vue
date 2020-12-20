<template>
  <el-row>
    <el-col :md="24">
      <el-card class="box-card div-causas-header">
        <el-table
          ref="multipleTable"
          v-loading="loading"
          :data="listaItems"
          style="width: 100%; border: 1px solid #d8ebff;"
          height="34vh"
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
  </el-row>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
// import ModalDelete from '@/components/ModalConfirm'
import { CONSTANTS } from '../constants/constants'
import { getListFacturaItems } from '@/api/unigrasas/factura-has-item'

export default {
  directives: { elDragDialog },
  components: {
    // ModalDelete
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
      vendedorEditar: this.editar
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
    }
  },
  async created() {
    this.getFacturaItems()
  },
  methods: {
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
