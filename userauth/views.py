#coding=utf-8
from django.shortcuts import render

# Create your views here.
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *

def user_login(request):

	return render_to_response('login.html')
#用户注销
def user_logout(request):
	del request.session['username']
	return render_to_response('login.html')

def change_password_index(request):
	return render_to_response('change_password_index.html')

def change_password(request):
	a=request.POST
	print a
	username=request.session['username']
	pw=a['pw']      
	print pw
	user.objects.filter(username=username).update(password=pw)
	return HttpResponse('修改成功')


#用户管理主页
def user_index(request):
	a=user.objects.all()
	username=request.session['username']
	role=user.objects.get(username=username).role	
	print "role-----"
	print role
	if role == 'admin':
		return render_to_response('user_index.html',{'a':a})
	else:
		return HttpResponse("对不起，您没有权限查看，请联系雷汉权")
###用户登录
def account_login(request):
	tem=request.POST
	username=tem['username']
	password=tem['password']
	request.session['username']=username
	
	sel_user=0
	sel_pass=0
	
	try:
		user1 = user.objects.get(username=username,password=password)
	except ObjectDoesNotExist:
		return HttpResponse("用户不存在或密码错误")

	print user1.active
	if user1.active == '0':
		return render_to_response("index.html",{'username':username})
	else:
		return HttpResponse("用户状态异常")

###用户增加 

def user_add(request):
	a=request.POST
	username=a['username']
	password=a['password']
	try:
		has_user=user.objects.get(username=username)
	except:
		has_user=False
	if has_user:
		return HttpResponse("用户已存在")
	else:

		user.objects.create(username=username,password=password,role='user',createtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),active='0')
		return HttpResponse('add successful')
	
###删除用户

def user_del(request):
	a=request.GET
	id=a['id']
	user.objects.filter(id=id).delete()
	return HttpResponse('delete successful')
	
