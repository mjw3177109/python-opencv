from django import forms


class BooStrap:

    boostrap_exclude_fields=[]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环找到所的插件
        for name, field in self.fields.items():
            if name in self.boostrap_exclude_fields:
                continue
            # 字段中有属性,保留原来的属性,没有属性,才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label

            else:
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}

class BootStrapModelForm(BooStrap,forms.ModelForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # 循环找到所的插件
    #     for name, field in self.fields.items():
    #         # 字段中有属性,保留原来的属性,没有属性,才增加
    #         if field.widget.attrs:
    #             field.widget.attrs["class"] = "form-control"
    #             field.widget.attrs["placeholder"] = field.label
    #
    #         else:
    #             field.widget.attrs = {"class": "form-control", "placeholder": field.label}

class BootStrapForm(BooStrap,forms.Form):
    pass