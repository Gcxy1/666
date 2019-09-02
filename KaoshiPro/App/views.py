import hashlib

from django.shortcuts import render, redirect,reverse

from App.forms import RegisterForm, LoginForm
from App.models import *


# 首页
def index(request):
    userid = request.session.get('userid',0)
    user = User.objects.filter(id = userid).first()
    shangbiao = Shangpin.objects.filter(type='1').first()
    nvtubiao = Shangpin.objects.filter(type='2').first()
    nvtuji = Shangpin.objects.filter(type='1-1').all()
    nantuleft = Shangpin.objects.filter(type='3').first()
    nantubiao = Shangpin.objects.filter(type='4').filter()
    nanturight = Shangpin.objects.filter(type='5').first()
    nantuji = Shangpin.objects.filter(type='2-2').all()
    data = {
        'shangbiao':shangbiao,
        'nvtubiao':nvtubiao,
        'nvtuji':nvtuji,
        'nantuleft':nantuleft,
        'nantubiao': nantubiao,
        'nanturight':nanturight,
        'nantuji': nantuji,
        'user':user,

    }
    print("*"*20)
    print(user)
    return render(request ,'index.html',data)

#注册
def register(request):
    if request.method == 'POST':
        print(222222222)
        #使用forms
         # 获取Form数据
        forms= RegisterForm(request.POST)
        #使用forms.is_valid()方法，对forms进行判断
        if forms.is_valid():  #判断forms的输入是否正确？
            #正确就获取数据，进行注册
            phone = forms.cleaned_data.get('phone')
            password = forms.cleaned_data.get('password')
            email = forms.cleaned_data.get('email')
            print("*"*30)
            print(phone)
            print(password)
            print(email)
            #注册cretae:添加
            User.objects.create(phone=phone,email=email,password=my_md5(password))

            return redirect(reverse('login'))
        else:
            #注册失败，返回form.errors
            return render(request,'register.html',{'errors':forms.errors})
    print(11111111)
    return render(request,'register.html')

def my_md5(s):
    #hashlib:设置密码加密：md5
    m = hashlib.md5()    #使用模块 hashlib,进行MD5加密
    m.update(s.encode())  # update，将参数添加给 m,进行加密操作。并且对参数转换编码格式 encode()
    return m.hexdigest()   #返回m值。并转换成十六进制字符串hex  digest() 【二进制字符串：digest（）]


#登录
def login(request):
    if request.method == 'POST':
        print('*'*23)
        print(111111111)
        #使用form，对获取的数据进行过滤、判断。在进行登录操作
        forms = LoginForm(request.POST)
         # 判断forms,输入的值是否正确？
        # print(forms.phone)
        # print(forms.password)
        print(forms,type(forms))
        if forms.is_valid():
            print(333333)
             #获取前端传给forms的值
            phone = forms.cleaned_data.get('phone')
            res = redirect(reverse('index'))
            request.session['userid'] = User.objects.first().id
            request.session.set_expiry(60*60*24) #设置过期时间为一天
            print(phone)
            return res
        print(forms.errors)
        return render(request,'login.html')
    else:
        return render(request,'login.html')

#注销session
def logout(request):
    #获取session
    res = redirect(reverse('index'))
    print(222222222)
    session_key = request.session.session_key
    print(session_key)
    request.session.delete(session_key)
    print(session_key)
    print(11111111111)
    return res