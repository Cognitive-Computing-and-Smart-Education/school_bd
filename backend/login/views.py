import json

from django.shortcuts import *
from login.models import *


def index(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get("password", None)
        # info = User.objects.values('user', 'password')
        #
        # print(info)
        print(username, password)
        # return 0
        pw = User.objects.filter(name=username).values()
        print(pw)
        if not username or not password:
            code = '失败！账号，密码不能为空'
        else:
            if pw:
                pw = pw[0]
                if password != pw['password']:
                    code = '失败！账号，密码错误！'
                else:
                    isAdmin = pw['isAdmin']
                    data = {
                        "isAdmin": isAdmin,
                        'username': username,
                    }
                    return HttpResponse(json.dumps(data))
            else:
                code = "失败！该账号不存在"
        return render(request, 'index.html', {'code': code})
