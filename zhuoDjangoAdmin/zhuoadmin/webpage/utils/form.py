
from  webpage.models import Admin
from django import forms
from django.forms import ModelForm
class AdminModelForms(ModelForm):
    class Meta:
        model = Admin
        # 这里是需要显示几个字段就填几个
        fields = ["userid", "password"]
