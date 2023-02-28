<template>
  <div>
    8888
  </div>
</template>

<script>
import {useRouter} from "vue-router";

export default {
  name: "LayOut",
  setup(){
    const router =useRouter()
    function goTo(){
      router.push({
        path:"/login"
      })
    }
    return{
      goTo
    }
  },

  created() {
    console.log("222")
    if(2>1){
      this.goTo()
    }
  },
}
</script>

<style scoped>

</style>