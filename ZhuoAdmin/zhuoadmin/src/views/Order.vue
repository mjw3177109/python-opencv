<template>
  <div>
    <el-table
        :data="tableDatas"
        style="width: 100%;border-radius: 5px;font-size: 12px">
      <el-table-column
          prop="id"
          label="序号"
          width="100">
      </el-table-column>
      <el-table-column
          prop="Orders"
          label="订单号"
          width="150">
      </el-table-column>

      <el-table-column
          prop="State"
          label="订单状态"
          width="130">
      </el-table-column>

      <el-table-column
          prop="Money"
          label="订单金额"
          width="100">
      </el-table-column>

      <el-table-column
          prop="Name"
          label="购买用户"
          width="130">
      </el-table-column>

      <el-table-column
          prop="Business"
          label="购买产品"
          width="130">

      </el-table-column>

      <el-table-column
          prop="Start_time"
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
</template>

<script>
export default {
name: "Order",
  data(){
  return{
    tableDatas:[],

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

    this.getData()

  },
  methods:{
    handleClick(row) {
      console.log(row);
    },

    getData(){
      let user =localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")):{};

      if (user){
        var tokens = user.token

      }else{
        tokens =""
      }

      this.request.get("/neworders/?token="+tokens).then(res=>{

        if (res.status ===200){
          this.tableDatas=res.data
          console.log(this.tableDatas)


        }else if(res.status === 987){
          this.$message.error("未登录或登录过期,请返回登录页面");

        }

      })

    },
  }
}
</script>

<style scoped>

*{
  margin:0;
  padding:0;

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