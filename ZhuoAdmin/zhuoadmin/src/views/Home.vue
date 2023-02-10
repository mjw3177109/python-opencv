<template>
  <div :style="{backgroundImage:'url('+require('../assets/background.png')+')'}" >

     <el-container style="min-height:100vh;min-width:100vw;">
          <el-header style="width:100%;height:64px;background: rgba(255, 255, 255, 1);padding:0">
            <Header style="width:100%;height:100%;"></Header>
          </el-header>
          <el-container style="width:100%;min-height:800px;padding-left:20px;padding-top:20px;overflow: auto;">
            <el-aside class="menu-left" style=" width: 220px;background: rgba(255, 255, 255, 0.2);">

              <el-menu
                  default-active="1-2"
                  :collapse="isCollapse"
                  default-act="opens"
                  class="el-menu-vertical-demo"
                  @open="handleOpen"
                  @close="handleClose"
                  style=" width:200px; margin-top:20px;border-radius:5px;margin-left: 10px;background:none;height: 300px;border: none"
              >


                <el-submenu index="1" style="text-align: left;line-height: 45px;color:#fff;background: none">
                  <template slot="title">
                    <span style="color:#fff;font-size: 16px;">业务管理</span>
                  </template>
                  <div style=" background: #57BC9A;border-radius:5px;width: 100%;height: 45px;">

                    <el-menu-item index="1-2" style="font-size: 16px;margin-left: -30px">

                      <img src="../assets/rightarrow.png" style="width: 15px;height: 15px;margin-top: -3px; margin-right: 5px"></img>订单管理</el-menu-item>
                  </div>

                </el-submenu>
              </el-menu>
            </el-aside>
            <el-main  class="menu-right" style=" min-width:1156px;">

              <div class="contentTable" style="width:100%;height:100%;background: rgba(255, 255, 255, 1);border-radius: 5px;padding-left:10px;">

                <el-table
                    :data="tableData"
                    style="width: 100%;border-radius: 5px;font-size: 12px">
                  <el-table-column
                      prop="id"
                      label="序号"
                      width="100">
                  </el-table-column>
                  <el-table-column
                      prop="orders"
                      label="订单号"
                      width="150">
                  </el-table-column>

                  <el-table-column
                      prop="state"
                      label="订单状态"
                      width="130">
                  </el-table-column>

                  <el-table-column
                      prop="price"
                      label="订单金额"
                      width="100">
                  </el-table-column>

                  <el-table-column
                      prop="user"
                      label="购买用户"
                      width="130">
                  </el-table-column>

                  <el-table-column
                      prop="product"
                      label="购买产品"
                      width="130">

                  </el-table-column>

                  <el-table-column
                      prop="create_time"
                      label="创建时间"
                      width="130">

                  </el-table-column>

                  <el-table-column
                      prop="update_time"
                      label="更新时间"
                      width="130">

                  </el-table-column>

                  <el-table-column

                      label="操作"
                      >
                    <template slot-scope="scope">
                      <el-button @click="handleClick(scope.row)" type="text" size="small" style="color:rgba(87, 188, 154, 1)">管理</el-button>
                      <el-button type="text" size="small" style="color:rgba(87, 188, 154, 1)">删除</el-button>
                    </template>
                  </el-table-column>




                </el-table>


              </div>


            </el-main>
          </el-container>

          <div class="pg-bottom">Copyright @ 2005-2021 ChueKan. All Rights Reserved</div>
    </el-container>


  </div>


</template>

<script>
import Header from "@/components/Header";

  export default {
   name: 'HomeView',
  components: {
    Header,
  },
    data () {
      return {msg: 'vue模板页',

        isCollapse: true,
        opens:1,
        tableData: [{
          id: '1',
          orders: 'CK20230206000001',
          state: '待支付',
          price:996.3,
          user:"何山河",
          product:"供灯",
          create_time:"2022/11/04 23:40",
          update_time:"2022/09/07 15:16",

        }, {
          id: '2',
          orders: 'CK20230206000002',
          state: '待支付',
          price:996.3,
          user:"何山河",
          product:"供灯",
          create_time:"2022/11/04 23:40",
          update_time:"2022/09/07 15:16",
        }, {
          id: '3',
          orders: 'CK20230206000003',
          state: '待支付',
          price:996.3,
          user:"何山河",
          product:"供灯",
          create_time:"2022/11/04 23:40",
          update_time:"2022/09/07 15:16",
        }, {
          id: '4',
          orders: 'CK20230206000004',
          state: '待支付',
          price:996.3,
          user:"何山河",
          product:"供灯",
          create_time:"2022/11/04 23:40",
          update_time:"2022/09/07 15:16",
        }],


      }
    },
    created() {
     this.Collapse()
    },
    methods:{

      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClick(row) {
        console.log(row);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      Collapse(){
        this.isCollapse=!this.isCollapse
      },


    }
  }
</script>
<!--css样式-->
<style>
    *{
      margin:0;
      padding:0;

    }

    .menu-left{

      border: 1px solid #EAEDF1;
      min-height:700px;
      overflow: auto;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(5px);





    }
    .el-menu{
      background: none;
    }

    .menu-right{


      background:rgba(255, 255, 255, 0.2);
      margin-left:20px;
      padding:20px;
      overflow:auto;
      min-height:700px;
      border-radius:10px;
      border: 1px solid #EAEDF1;

    }
    .el-menu .el-submenu:hover{
      background:none;
    }

    .el-menu .el-submenu:focus {
      background:none;
    }
    .el-menu .el-submenu__title:focus{
      background:none;
    }
    .el-menu .el-submenu__title:hover {
      background: none;
    }
    .el-menu .el-submenu__title i {
      color: #fff;
    }
    .el-menu .el-submenu .el-menu{
      background: none;
    }

    .el-menu .el-submenu .el-menu  .el-menu-item.is-active{
      color: #FFFFFF;
    }

    .el-menu .el-submenu .el-menu .el-menu-item:focus {

      background:none;
    }

    .el-menu .el-submenu .el-menu .el-menu-item:hover {

      background:none;
    }
    .pg-bottom{
      width:100%;
      height:64px;
      line-height:64px;
      text-align:center;
      background:#FFFFFF;
      color:rgba(0, 0, 0, 0.4);

    }
</style>
