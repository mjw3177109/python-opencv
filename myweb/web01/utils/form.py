import re
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from web01.utils.encrypt import md5
from web01.utils.boostrap import BootStrapModelForm,BootStrapForm
from web01.models import Department, UserInfo, UserInfoTable, PrettyNum,Admin,Task,Order




class UserModelForms(BootStrapModelForm):
    name = forms.CharField(min_length=2, label="用户名")

    class Meta:
        model = UserInfoTable
        fields = ["name", "password", "age", "create_time", "gender", "depart"]


class PrettyModelForm(BootStrapModelForm):
    # 验证方式一 正则方法
    mobile = forms.CharField(label="手机号", validators=[RegexValidator(r"^1[3-9]\d{9}$", "手机号格式错误")])

    class Meta:
        model = PrettyNum
        fields = ["mobile", "price", "level", "status"]

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #
    #     #循环找到所的插件
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {"class": "form-control","placeholder":field.label}

    # 验证方式2 钩子方法
    # def clean_mobile(self):
    #     complie=re.compile(r"^1[3-9]\d{9}$")
    #     txt_moblie =self.cleaned_data["mobile"]
    #     row_object =PrettyNum.objects.filter(mobile=txt_moblie)
    #     if len(row_object)>=1:
    #         raise ValidationError("号码已存在")
    #     if len(txt_moblie) !=11:
    #         raise ValidationError("格式错误")
    #     elif not complie.match(txt_moblie):
    #         raise ValidationError("格式错误")
    #     return txt_moblie
    def clean_mobile(self):
        txt_moblie = self.cleaned_data["mobile"]
        # exists =PrettyNum.objects.filter(mobile=txt_moblie).exists()
        print(self.instance.pk)
        exists = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_moblie).exists()
        if exists:
            raise ValidationError("号码已存在")

        # complie = re.compile(r"^1[3-9]\d{9}$")
        # if not complie.match(txt_moblie):
        #     raise ValidationError("格式错误")
        return txt_moblie


class PrettyEditForm(BootStrapModelForm):
    # 显示不可修改
    # mobile =forms.CharField(disabled=True)
    class Meta:
        model = PrettyNum
        fields = ["price", "level", "status"]
        # fields = ["price", "level", "status"]

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #
    #     #循环找到所的插件
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {"class": "form-control","placeholder":field.label}


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码",widget=forms.PasswordInput)
    class Meta:
        model = Admin
        fields = ["username", "password","confirm_password"]
        widgets={
            "password":forms.PasswordInput
        }
    def clean_password(self):
        pwd =self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        print(pwd)
        confirm = md5(self.cleaned_data.get("confirm_password"))
        print(confirm)
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm




class AdminEditForm(BootStrapModelForm):
    class Meta:
        model = Admin
        fields = ["username"]




class AdminResetForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput)
    class Meta:
        model=Admin
        fields =["password","confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }


    def clean_password(self):
        pwd =self.cleaned_data.get("password")
        md5_pwd=md5(pwd)

        #去数据库校验密码是否和原密码一致
        exists = Admin.objects.filter(id=self.instance.pk,password=md5_pwd).exists()
        if exists:
            raise  ValidationError("密码不能和之前的密码一致")
        return md5_pwd

    def clean_confirm_password(self):
        print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        print(pwd)
        confirm = md5(self.cleaned_data.get("confirm_password"))
        print(confirm)
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm


# class LoginForm(forms.Form):
    # username = forms.CharField(label="用户名",widget=forms.TextInput(attrs={"class":"form-control"}))
    # password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={"class":"form-control"}))

class LoginForm(BootStrapForm):
    username = forms.CharField(label="用户名",widget=forms.TextInput,required=True)
    password = forms.CharField(label="密码", widget=forms.PasswordInput(render_value=True),required=True)
    code = forms.CharField(label="验证码", widget=forms.TextInput, required=True)
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model =Task
        fields ="__all__"
        widgets = {
            "detail": forms.TextInput
        }


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model =Order
        #fields= "__all__"
        exclude = ["oid","admin"]

