<template>
  <div>
    <el-collapse-transition>
      <div v-show="showElements" style="padding-bottom: 10px">
        <sticky class-name="sub-navbar">
          <div style="text-align: center; color: white">
            <el-row>
              <el-col :span="20" style="padding-left: 15%;">
                <label style="font-size: x-large">Factura N° {{ id }}</label>
              </el-col>
              <el-col :span="4">
                <!-- Div Botones -->
                <el-button
                  style="border: 2px solid #67c23a"
                  size="medium"
                  icon="el-icon-printer"
                  @click="fetchData()"
                >Imprimir</el-button>
                <el-button
                  style="border: 1px solid #67c23a"
                  type="warning"
                  size="medium"
                  @click="closeWindow()"
                >Cerrar</el-button>
              </el-col>
            </el-row>
          </div>
        </sticky>
      </div>
    </el-collapse-transition>
    <div
      v-loading.fullscreen.lock="fullscreenLoading"
      class="main-article"
      element-loading-text="Generando PDF..."
      :style="showElements ? {border: '1px solid #E4E7ED', marginTop: '2%'} : {}"
    >
      <div :style="showElements ? {padding: '3%'} : {}">
        <!-- encabezado -->
        <el-row>
          <el-col :span="7" style="padding-top: 2.8%;">
            <img :src="logo" class="logo">
          </el-col>
          <el-col :span="17">
            <el-row>
              <el-col :span="24" style="font-size: 11px; padding-left: 2.5%; padding-bottom: 1%;"><b>UNIGRASAS COLOMBIA S.A.S</b></el-col>
              <div style="font-size: 10px; padding-left: 2.5%;">
                <el-col :span="24" style="padding-bottom: 0.5%;">NIT: 830090675-7</el-col>
                <el-col :span="24" style="padding-bottom: 0.5%;">Régimen: Responsable del impuesto sobre las ventas –IVA</el-col>
                <el-col :span="24" style="padding-bottom: 0.5%;">Persona Jurídica</el-col>
                <el-col :span="24" style="padding-bottom: 0.5%;">Carrera 97 # 24c-50.5, BOGOTÁ, D.C., Bogotá, Colombia</el-col>
                <el-col :span="24" style="padding-bottom: 0.5%;">Tel. 3507259492</el-col>
                <el-col :span="24" style="padding-bottom: 0.5%;">AUTORIZACIÓN FACTURA ELECTRÓNICA DE VENTA No. 0.58764002623347 VÁLIDA DESDE 2020-08-20</el-col>
                <el-col :span="24" style="padding-bottom: 0.5%;">HASTA 2021-08-20 RANGO DESDE FELE1 HASTA FELE1000</el-col>
              </div>
            </el-row>
          </el-col>
        </el-row>
        <!-- separador -->
        <div style="border-top: 1px solid #DCDFE6; margin-top: 2%;" />
        <!-- datos generales -->
        <el-row style="margin-top: 2.5%;">
          <el-col :span="12" style="border: 1px solid; border-radius: 5px; padding: 1.5%;">
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="5" style="font-size: 10.5px;"><b>Cliente: </b></el-col>
              <el-col :span="19" style="font-size: 10.5px;">YANID SALAS OLARTE</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="5" style="font-size: 10.5px;"><b>Nit: </b></el-col>
              <el-col :span="19" style="font-size: 10.5px;">26553956.3</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="5" style="font-size: 10.5px;"><b>Dirección: </b></el-col>
              <el-col :span="19" style="font-size: 10.5px;">CL 22 SUR 2 72, PITALITO, Huila, COLOMBIA</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="5" style="font-size: 10.5px;"><b>Teléfono: </b></el-col>
              <el-col :span="19" style="font-size: 10.5px;">3132434489</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="5" style="font-size: 10.5px;"><b>Email: </b></el-col>
              <el-col :span="19" style="font-size: 10.5px;">yanid0905@hotmail.com</el-col>
            </el-row>
            <div style="border-top: 1px solid #606266; margin-top: 1.5%; padding-bottom: 1.5%;" />
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="9" style="font-size: 10.5px;"><b>Tipo de negociación: </b></el-col>
              <el-col :span="15" style="font-size: 10.5px;">Crédito</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="9" style="font-size: 10.5px;"><b>Medio de Pago: </b></el-col>
              <el-col :span="15" style="font-size: 10.5px;">Transferencia Crédito</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5%;">
              <el-col :span="9" style="font-size: 10.5px;"><b>Fecha de Pago: </b></el-col>
              <el-col :span="15" style="font-size: 10.5px;">17/09/2020</el-col>
            </el-row>
          </el-col>
          <el-col :span="1">
            &nbsp;
          </el-col>
          <!-- datos facturacion -->
          <el-col :span="11" style="border: 1px solid; border-radius: 5px; padding: 1.5%;">
            <el-row style="padding-bottom: 0.5%; border-bottom: 1px solid #606266;">
              <el-col :span="10" style="font-size: 10.5px; color: #ff4603;"><b>FACTURA DE VENTA: </b></el-col>
              <el-col :span="14" style="font-size: 10.5px;"><b>FELE15</b></el-col>
            </el-row>
            <el-row style="padding-top: 0.5%; border-bottom: 1px solid #606266;">
              <el-col :span="10" style="font-size: 10.5px; color: #ff4603;"><b>MONEDA: </b></el-col>
              <el-col :span="14" style="font-size: 10.5px;"><b>COP Colombia, Pesos</b></el-col>
            </el-row>
            <el-row style="padding-top: 0.5%; border-bottom: 1px solid #606266;">
              <el-col :span="10" style="font-size: 10.5px; color: #ff4603;"><b>HORA EMISIÓN: </b></el-col>
              <el-col :span="14" style="font-size: 10.5px;"><b>10:44:45</b></el-col>
            </el-row>
            <el-row style="padding-top: 0.5%; border-bottom: 1px solid #606266;">
              <el-col :span="10" style="font-size: 10.5px; color: #ff4603;"><b>FECHA FIRMADO: </b></el-col>
              <el-col :span="14" style="font-size: 10.5px;"><b>20/09/2020 15:44:43</b></el-col>
            </el-row>
            <el-row :gutter="10" style="text-align: center;">
              <!-- fecha emision -->
              <el-col :span="12">
                <el-row>
                  <el-col :span="24" style="font-size: 11px; padding-top: 7%; padding-bottom: 7%;"><b>FECHA DE EMISIÓN</b></el-col>
                  <el-col :span="24" class="table-fechas">
                    <table>
                      <tr class="fecha-th">
                        <th>DIA</th>
                        <th>MES</th>
                        <th>AÑO</th>
                      </tr>
                      <tr class="fecha-td">
                        <td>17</td>
                        <td>09</td>
                        <td>2020</td>
                      </tr>
                    </table>
                  </el-col>
                </el-row>
              </el-col>
              <!-- fecha emision -->
              <el-col :span="12">
                <el-row>
                  <el-col :span="24" style="font-size: 11px; padding-top: 7%; padding-bottom: 7%;"><b>FECHA DE EMISIÓN</b></el-col>
                  <el-col :span="24" class="table-fechas">
                    <table>
                      <tr class="fecha-th">
                        <th>DIA</th>
                        <th>MES</th>
                        <th>AÑO</th>
                      </tr>
                      <tr class="fecha-td">
                        <td>17</td>
                        <td>09</td>
                        <td>2020</td>
                      </tr>
                    </table>
                  </el-col>
                </el-row>
              </el-col>
            </el-row>
          </el-col>
        </el-row>
        <!-- items -->
        <el-row style="margin-top: 2.5%;">
          <el-col :span="24" class="wrapper">
            <table class="table-items">
              <tr class="items-th">
                <th># </th>
                <th>CÓDIGO</th>
                <th>DESCRIPCIÓN</th>
                <th>CANTIDAD</th>
                <th>PRECIO U.</th>
                <th>TOTAL</th>
              </tr>
              <tr class="items-td">
                <td>1</td>
                <td>0201011</td>
                <td>MARGARINA INDUSTRIAL A.Te T.F</td>
                <td>207</td>
                <td>57.142,86</td>
                <td>11.828.572,02</td>
              </tr>
            </table>
          </el-col>
        </el-row>
      </div>
    </div>
    <div :style="showElements ? {display: 'block'} : {}">
      <br><br>
    </div>
  </div>
</template>

<script>
import Sticky from '@/components/Sticky' // 粘性header组件
import logoEmpresa from '@/assets/unigrasas.jpg'

export default {
  name: 'ViewPdf',
  components: { Sticky },
  data() {
    return {
      logo: logoEmpresa,
      article: '',
      fullscreenLoading: false,
      id: '',
      showElements: true
    }
  },
  mounted() {
    this.id = this.$route.params.id
    console.log('Imprimir factura -> ', this.id)
  },
  methods: {
    fetchData() {
      this.showElements = false
      this.fullscreenLoading = true
      import('./content.js').then((data) => {
        console.log(data)
        const { title } = data.default
        document.title = title
        console.log('document -> ', document)
        this.article = data.default
        setTimeout(() => {
          this.fullscreenLoading = false
          this.$nextTick(() => {
            window.print()
            this.showElements = true
          })
        }, 500)
      })
    },
    closeWindow() {
      // this.$router.push({ path: `/procesos/facturas` })
      this.$router.go(-1)
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');
.logo {
  width: 93%;
}
.main-article {
  // padding: 20px;
  font-family: 'Roboto', sans-serif;
  margin: 0 auto;
  display: block;
  width: 740px;
  background: white;
}

.table-fechas table {
  border: 1px solid black;
  border-collapse: collapse;
  width: 100%;
}

.fecha-th th {
  padding: 1%;
  color: #C0C4CC;
  font-size: 10px;
  border: 1px solid black;
}

.fecha-td td {
  font-size: 11px;
  border: 1px solid black;
}

.wrapper {
  overflow: auto;
  border-radius: 6px;
  border: 1px solid black;
}

.table-items {
  border-spacing: 0;
  border-collapse: collapse;
  border-style: hidden;
  width:100%;
  max-width: 100%;
}

.items-th th {
  padding: 1%;
  font-size: 10px;
  border: 1px solid black;
}

.items-td td {
  padding-top: 2%;
  padding-bottom: 2%;
  font-size: 11px;
  border: 1px solid black;
  text-align: center;
}
</style>
