from django.test import TestCase

# Create your tests here.
from login.models import LoginUser, LoginGroup

# 查询结果返回对象
# users = LoginUser.objects.all()
# groups = LoginGroup.objects.all()

# for user in users:
#     print(user.name, user.password, user.sex)
#
# for group in groups:
#     print(group)

# 查询结果返回字典
# users = LoginUser.objects.values('name',  "sex")
# groups = LoginGroup.objects.values()
# for user in users:
#     print(user)
#
# for group in groups:
#     print(group)

# 查询结果返回元组(4,5,6)
# users = LoginUser.objects.values_list('name',  "sex")
# groups = LoginGroup.objects.values_list()
# for user in users:
#     print(user)
#
# for group in groups:
#     print(group)


# 查询结果排序
users = LoginUser.objects.order_by("sex").values()
groups = LoginGroup.objects.order_by().values()
for user in users:
    print(user)

for group in groups:
    print(group)


users = LoginUser.objects.order_by("-sex")
print(users.query)