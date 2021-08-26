from django.shortcuts import render
from login.models import *


def index(request):
    return render(request, 'index.html')


# Create your views here.
def datail(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get("password", None)
        message = "所有字段都必须填写"
        if username and password:
            username = username.strip()
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    return render(request, 'detail.html')
                else:
                    return render(request, "index.htmll", {'error': "密码不正确!"})
            except:
                return render(request, "index.htmll", {'error': "账号不存在!"})
        else:
            return render(request, "index.htmll", {'error': "账号密码不能为空!"})
