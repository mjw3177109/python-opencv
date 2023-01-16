
"""
 自定义分页组件
#1.请求的对象
即使django的request对象
#2.根据自己的方法去筛选数据
queryset = PrettyNum.objects.all()
#3.设定分页的大小 即每一页显示多少条
page_size=5
#4.获取分页的当前页参数
pagenum=1
#5.设定页码每一次显示多少页
plus=5
即使显示当前页码的前五和后五页码

在html中添加
  <ul class="pagination"> #class 来自boostrap 要在公共文件自己引入

             {{page_string}}
  </ul>





"""
from django.utils.safestring import mark_safe
class Pageination(object):


    def __init__(self,request,queryset,page_param="pagenum",page_size=1,plus=5):

        from django.http.request import  QueryDict
        import copy
        query_dict =copy.deepcopy(request.GET)
        query_dict._mutable= True
        self.query_dict=query_dict
        self.page_param=page_param
        page = request.GET.get(page_param,"1")
        if page.isdecimal():
            page =int(page)
        else:
            page =1
        print(page,type(page))
        self.page =page
        self.page_size =page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.queryset =queryset[self.start:self.end]
        #总页数
        data_all_num =queryset.count()
        total_page, div = divmod(data_all_num, page_size)
        if div:
            total_page += 1
        self.total_page =total_page
        self.plus =plus


    def html(self):
        # 计算出应该显示当前页的第五页和后五页

        #plus = 5


        if self.total_page <= 2 * self.plus + 1:
            # 数据库中的数据比较少
            start_page = 1
            end_page = self.total_page
        else:
            # 当页面小于5的极值
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页大于极值
                if self.page + self.plus > self.total_page:
                    start_page = self.total_page - 2 * self.plus
                    end_page = self.total_page
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        #print(self.query_dict.urlencode())

        # 首页
        page_str_list.append('<li ><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))
        # 上一页
        if self.page == 1:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li ><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li ><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())

        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li ><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            after = '<li ><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page])
            after = '<li ><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())

        page_str_list.append(after)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page])
        page_str_list.append('<li ><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        page_str_goto = """
         <li>
              <form style="float:left;margin-left:-1px" method="get">
                     <input type="text" class="form-control" placeholder="页码" name="pagenum" style="position:relative; float:left; display:inline-block; width:80px;border-radius:0;">
                     <button class="btn btn-default" type="submit" style="border-radius:0">跳转</button> 
               </form>  
         </li>  
         """
        page_str_list.append(page_str_goto)

        page_string = mark_safe("".join(page_str_list))

        return page_string

