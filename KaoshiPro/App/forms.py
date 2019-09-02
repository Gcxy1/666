import hashlib
import re

from django import forms


from App.models import User

#验证注册
class RegisterForm(forms.Form):
    phone = forms.CharField(
        required= True,
        max_length=11,
        min_length=11,
        error_messages={
            'required':'注册用户手机号必须填写',
        },
    )
    password = forms.CharField(
        required=True,
        max_length=20,
        min_length=8,
        error_messages={
            'required':'注册用户的密码必须填写',
            'max_length':'密码最大不能大于20',
            'min_length':'密码最小不能少于8',
        },
    )
    password2 = forms.CharField(
        required=True,
        max_length=20,
        min_length=8,
        error_messages ={
            'required':'确认密码必须填写',
            'max_length':'确认密码最大不能大于20',
            'min_length':'确认密码最小不能小于8',
        },
    )
    email = forms.CharField(
        required=True,
        error_messages={
            'required':'注册邮箱必须填写',
        },
    )

    # 重新clean方法，再次过滤数据
    def clean(self):
        # 获取初步过滤数据
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')

        #二次判断，判断输入的字段是否为空
        if not phone:
            raise forms.ValidationError({'phone':'电话号码不能为空'})
        if not password:
            raise forms.ValidationError({'password':'密码不能为空'})
        if not password2:
            raise forms.ValidationError({'password':'确认密码不能为空'})
        if  not email:
            raise forms.ValidationError({'email':'邮箱不能为空'})

        #三次判断，（两次密码是否一致，电话号码是否为数字，邮箱是否合法，用户是否存在于数据库）
        if password2 != password:   #如果两次输入密码不一致，抛出异常
            raise forms.ValidationError({'password2':'两次密码输入不一致！'})

        try:
            if  not re.search(r'^\w{11}$',phone):
                raise forms.ValidationError({'phone':'电话号码输入有误！'})
        except:
            raise forms.ValidationError({'phone':'电话号码输入有误！'})

        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError({'phone':'用户已存在！'})

        if not re.search(r'^\w+@\w+\.(com|cn)$',email):
            raise forms.ValidationError({'email':'邮箱输入不合法！'})

        return self.cleaned_data


# 验证登录
class LoginForm(forms.Form):
    phone = forms.CharField(
        required=True,
        max_length=11,
        min_length=11,
        error_messages={
          'required':'登录号码必须填写',
          'max_length':'电话号码最长不能超过11',
          'min_length':'电话号码最短不能少于11',
        },
    )
    password = forms.CharField(
        required=True,
        max_length='20',
        min_length='8',
        error_messages={
            'required':'登录密码必须填写',
            'max_length':'密码最长不能超过20',
            'min_length':'密码最短不能少于8',
        },
    )
    #重写 clean方法
    def clean(self):
        # 获取过滤后的数据
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')

        # 二次过滤字段
        if not phone:  # raise:抛出异常信息：ValidationError
            raise forms.ValidationError({'phone':'用户不能为空！'})
        if not password:
            raise forms.ValidationError({'password':'密码不能为空'})

        # 再次判断：(判断电话号码输入格式是否正确、判断用户是否存在，判断输入密码是否正确)
        try:
            if  not re.search(r'^\w{11}$', phone):
                raise forms.ValidationError({'phone':'输入格式有误'})
        except:
            raise forms.ValidationError({'phone':'输入格式有误!'})

        if not User.objects.filter(phone=phone).exists():
            raise forms.ValidationError({'phone':'电话号码不能为空'}) #获取错误信息：ValidationError

        if not User.objects.filter(phone=phone,password=my_md5(password)).exists():
            raise forms.ValidationError({'password':'密码输入有误！'})

        return self.cleaned_data
def my_md5(s):
    m = hashlib.md5()  #导入加密模板
    m.update(s.encode()) #添加需要加密的参数s,并转换编码格式encode()
    return m.hexdigest()  # 将加密后的值返回，并转换为十六进制的字符串
