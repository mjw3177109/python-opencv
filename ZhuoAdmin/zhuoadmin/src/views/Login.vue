<template>
  <div :style="{backgroundImage:'url('+require('../assets/background.png')+')'}">
    <el-container style="min-height:100vh;min-width:100vw;" >

      <el-header style="width:100%;height:64px;background: rgba(255, 255, 255, 1);padding:0">
        <div style="width: 100%;height:100%">
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
          </div>
      </el-header>

      <div class="pg-body" style="width:100%;min-height:800px; overflow:hidden;">
           <div class="account">
             <div style="color:#fff;font-size:16px;text-align: left"><span style="border-bottom:2px solid rgba(161, 210, 255, 1); padding-bottom:5px;">账户密码登录</span></div>

             <el-form :model="user" ref="userForm" style="margin-top: 20px;">
               <el-form-item prop="username" style="margin-top: 25px">
                 <el-input size="medium"    v-model="user.userid" style="height:40px;" placeholder="用户名"></el-input>
               </el-form-item>

               <el-form-item  prop="password" style="margin-top: 25px" >
                 <el-input size="medium"  type="password" v-model="user.password" style="height:40px;" placeholder="密码"></el-input>
               </el-form-item>

               <el-form-item style="margin-top:40px;text-align: right">
                 <el-button type="primary" size="small" onautocomplete="off" @click="login" style="width: 100%;background: #57BC9A;
border-radius: 2px;color:rgba(255, 255, 255, 1);height:40px;text-align: center;font-size: 16px">登录</el-button>
               </el-form-item>

               <span style="color:red">{{error_msg}}</span>

             </el-form>





           </div>

      </div>

      <div class="pg-bottom">Copyright @ 2005-2021 ChueKan. All Rights Reserved</div>


    </el-container>

  </div>





</template>

<script>
export default {
name: "Login",
  data(){
  return{
    bg2: '../assets/background.png',
    user:{},
    error_msg:"",

    rules:{


    }
  }
  },
  methods:{
    login(){
      this.request.post("/newlogin/",this.user).then(res=>{

        if(res.status=="200" && res.error_msg===""){
          console.log(res.data)

          this.$router.push("/")
          localStorage.setItem("user",JSON.stringify(res.data)) //保存用户信息
          this.$message.success("登录成功")
          console.log(res.data)


        }else{


          this.$message.error(res.error_msg);
        }
      })
    }
  },
}
</script>

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


.pg-bottom{
  width:100%;
  height:64px;
  line-height:64px;
  text-align:center;
  background:#FFFFFF;
  color:rgba(0, 0, 0, 0.4);

}
.account{
  width:410px;
  height:323px;
  margin-left:auto;
  margin-right: auto;
  margin-top:160px;
  padding:20px 40px;
  position:relative;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(5px);
  border-radius: 10px;


}

.el-input--medium .el-input__inner {
  height: 40px;
  line-height: 40px;
}

</style>