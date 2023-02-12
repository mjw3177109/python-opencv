<template >
    <div>
    <div class="left_header">
       <img class="logo" src="../assets/zhuo.png">
       <div class="TextName">
             <div class="topTitle">
                 深圳市卓勤新技术发展有限公司
             </div>
              <div class="bottomTitle">
                  ShenZhen ChueKan New Technology Developments Co,.Ltd
              </div>
       </div>
    </div>

     <el-dropdown class="avauterRight">
         <div style="display: inline-block">
           <img src="../assets/default.png" style="width: 38px;border-radius: 50%;position: relative;top:10px;right: 35px">
         </div>
         <el-dropdown-menu slot="dropdown" style="width: 70px;text-align: center;margin-left:10px">
           <el-dropdown-item style="font-size: 14px;padding:0 0 ">个人信息</el-dropdown-item>
           <el-dropdown-item style="font-size: 14px;padding: 0 0">
           <span  style="text-decoration: none" @click="logout">退出</span>
           </el-dropdown-item>
         </el-dropdown-menu>
   </el-dropdown>

    </div>
</template>


<script>
import store from "@/store";
export default {
  name: "Header",
    data () {
      return {msg: 'vue模板页'}
    },
  methods:{
    logout(){
      this.$router.push("/login/")
      localStorage.removeItem("user")
      this.$message.success("退出成功");
    },
  }
  }
</script>
<!--css样式-->
<style scoped>

.left_header{
   width:570px;
   height:64px;
   padding-left:20px;
   float:left;
   overflow: visible;


}
.left_header .TextName{
        width:480px;

        height:64px;

        float:left;
        margin-left:8px;
        color:#000000;

}

.left_header .TextName .topTitle{
          height:48px;
          font-size:24px;
          line-height:51px;
          text-align:left;

}
.left_header .TextName .bottomTitle{
          height:16px;
          padding-left:18px;
          font-size:12px;
          margin-top:-5px;
           text-align:left;

}

.left_header .logo{
        height:52px;
         width:52px;
         line-height:52px;
         float:left;
         margin-top:5px;

}
.avauterRight{
  float:right;
  height:48px;
  line-height:48px;

  min-width:120px;

  cursor: pointer;
  text-align: right;
  margin-top:2px;

}


</style>