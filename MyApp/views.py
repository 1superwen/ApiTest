from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from MyApp.models import *


@login_required
def welcome(request):
    return render(request, 'welcome.html')

# 返回子页面
def child(request, eid, oid):

    res = child_json(eid)

    return render(request, eid, res)

# 控制不同的页面返回不同的数据：数据分发器
def child_json(eid):
    res = {}
    if eid == 'Home.html':
        data = DB_home_href.objects.all()
        res = {"hrefs": data}
    if eid == 'project_list.html':
        data = DB_project.objects.all()
        res = {"projects": data}
    return res



# 进入主页
@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "Home.html", "oid": ""})

def login(request):
    return render(request, 'login.html')

def login_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    # 开始 联通 django 用户库，查看用户密码是否正确
    from django.contrib import auth
    user = auth.authenticate(username=u_name, password=p_word)
    if user is not None:
        # 进行正确的动作
        auth.login(request, user)
        request.session['user'] = u_name
        return HttpResponse('成功')
    else:
        # 返回前端告诉前端用户名和密码不对
        return HttpResponse('失败')

def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    # 开始 联通django用户表
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=u_name, password=p_word)
        user.save()
        return HttpResponse('注册成功')
    except:
        return HttpResponse('注册失败~用户名好像已经存在了~')

def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')

# 吐槽函数
def pei(request):
    tucao_text = request.GET['tucao_text']

    DB_tucao.objects.create(user=request.user.username, text=tucao_text)
    return HttpResponse('')

# 帮助文档
@login_required
def api_help(request):
    return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})

def project_list(request):
    return render(request, 'welcome.html', {"whichHTML": "project_list.html", "oid": ""})

# 删除项目
def delete_project(request):
    id = request.GET['id']

    DB_project.objects.filter(id=id).delete()

    return HttpResponse('')
# 新增项目
def add_project(request):
    project_name = request.GET['project_name']
    DB_project.objects.create(name=project_name, remark='', user=request.user.username, other_user='')
    return HttpResponse('')