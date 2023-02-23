from django.utils.deprecation import  MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect

class AuthMiddleware(MiddlewareMixin):
    """ 中间件1"""

    def process_request(self,request):
        #0.排除不需要登录就访问的页面
        #request.path_info #获取当前用户请求的url /login/
        if request.path_info in ["/login/","/newlogin/","/neworders/","/test/","/newtest/","/getMusic/","/getChan/"]:
            return
        #1.读取当前访问的用户的session信息,如果能读到,说明已登录过就可以继续向后走,如果没有说明没登录
        info=request.session.get("info")
        if info:
            return
        else:
            return redirect("/login/")

