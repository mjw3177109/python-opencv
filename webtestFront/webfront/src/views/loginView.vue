<template>
   <div class="login-body">
      <div class="login-win">
          <div class="login-form">
              <Form ref="loginForm" id="newdform" :rules="rules" :model="loginForm" :label-width="30">
                  <h3 style="font-size: 24px;margin-bottom: 30px;padding-top:20px">学生在线考试系统</h3>
                  <FormItem prop="userName" class="newItems" >
                       <Input v-model="loginForm.userName" placeholder="请输入您的账号..." style="width: 100%;"></Input>
                  </FormItem>

                  <FormItem prop="passWord" class="newItems">
                       <Input type="password"  v-model="loginForm.passWord"  placeholder="请输入您的密码" style="width: 100%"></Input>
                  </FormItem>

                  <FormItem style="margin-top: 40px;margin-left: -43px;">
                      <Button style="width:226px;" @click="submitForm('loginForm')" class="login-btn" type="primary">
                         用户登录
                      </Button>


                  </FormItem>

              </Form>
          </div>
      </div>


   </div>
</template>

<script>
import {useRouter} from 'vue-router'
export default {
  name: 'loginView',
  setup(){
    const router =useRouter()
    function goTo(){
      router.push({
        path:"/"
      })
    }
    return{
      goTo
    }
  },


  data(){
   return{
     loginForm:{},
      rules:{
        userName: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        passWord: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
        ]


    },

   }
  },
  methods:{

    submitForm(loginInfo){
     this.goTo()
    }
  }
}
</script>


<style scoped>

.login-body{
  height:100vh;
  width:100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  background: url("~@/assets/hero-bg.jpg") no-repeat;



}

.login-body .login-win{
   width:400px;
   height:300px;

}

.login-body .login-win .login-form{
  width:100%;
  height: 100%;


}
.login-body .login-win .login-form #newdform{

  width:100%;
  height: 100%;
  background: #fff;
  opacity: 0.8;


  border-radius: 5px;
}

.login-body .login-win .login-form #newdform .newItems{
  width: 100%;
  padding-right: 30px;
  height: 40px;

}

.login-body .login-win .login-form #newdform .newItems .ivu-form-item-content{
  margin-left: 0px;
}




.login-body .login-win .login-form #newdform .newItems >>> .ivu-input{
  height: 40px;
}
</style>
