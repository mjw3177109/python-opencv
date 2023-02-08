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

<!--                <el-submenu index="1" style="text-align: left;line-height: 45px;color:#fff">-->
<!--                  <template slot="title">-->
<!--                    <span style="color:#fff">业务管理</span>-->
<!--                  </template>-->
<!--                  <el-menu-item-group>-->
<!--                    <el-menu-item index="1-2">选项2</el-menu-item>-->
<!--                  </el-menu-item-group>-->
<!--                  <el-menu-item-group>-->
<!--                    <el-menu-item index="1-3">选项3</el-menu-item>-->
<!--                  </el-menu-item-group>-->
<!--                </el-submenu>-->
              </el-menu>







            </el-aside>
            <el-main  class="menu-right" style=" min-width:1156px;">





            </el-main>
          </el-container>
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
      }
    },
    created() {
     this.Collapse()
    },
    methods:{

      handleOpen(key, keyPath) {
        console.log(key, keyPath);
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
</style>
