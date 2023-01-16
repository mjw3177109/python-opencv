from django.utils.deprecation import  MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect

class AuthMiddleware(MiddlewareMixin):
    """ 中间件1"""

    def process_request(self,request):


        #0.排除不需要登录就访问的页面
        #request.path_info #获取当前用户请求的url /login/
        if request.path_info in ["/login/","/image/code/"]:
            return
        #1.读取当前访问的用户的session信息,如果能读到,说明已登录过就可以继续向后走,如果没有说明没登录
        info=request.session.get("info")

        if info:
            return
        else:

            #2.没有登录
            # return redirect("/login/")
            return redirect("/login/")


        #如果方法中没有返回值就继续往下走 有就不继续
        # print("M1.进来了")
       # return HttpResponse("无权访问")

    # def process_response(self,request,response):
    #     print("M1 走了")
    #     return response


# class M2(MiddlewareMixin):
#     """ 中间件2"""
#
#     def process_request(self, request):
#         print("M2.进来了")
#
#     def process_response(self, request, response):
#         print("M2 走了")
#         return response
