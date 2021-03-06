#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from django.contrib.auth import authenticate
from django.utils.datastructures import MultiValueDictKeyError
from zichanmanager.userauth.models import *

# Create your views here.


def phone_info(request):
	jieguo=phoneinfo.objects.filter(baofei='1')
	a=request.GET
	username=request.session['username']
	role=user.objects.get(username=username).role
	if a:
		find_con=a['curuser']
		if find_con:
			jieguo=phoneinfo.objects.filter(curuser=find_con)
	else:
		jieguo=phoneinfo.objects.filter(baofei='1')
	return render_to_response('phone_info.html',{'a':jieguo,'role':role})

def phoneinfo_add(request):
    a=request.POST
    print a
    numbers=a['numbers']
    mingcheng=a['mingcheng']
    pinpai=a['pinpai']
    xinghao=a['xinghao']
    chicun=a['chicun']
    banbeninfo=a['banbeninfo']
    peijian=a['peijian']
    zhishi=a['zhishi']
    bianhao=a['bianhao']
    curuser=a['curuser']
    bumen=a['bumen']
    beizhu=a['beizhu']
    phoneinfo.objects.create(numbers=numbers,mingcheng=mingcheng,pinpai=pinpai,xinghao=xinghao,chicun=chicun,banbeninfo=banbeninfo,peijian=peijian,zhishi=zhishi,bianhao=bianhao,curuser=curuser,bumen=bumen,beizhu=beizhu)
    return HttpResponse('add successful')
    #return render_to_response('phoneinfo_add.html')

def phoneinfo_del(request):
        a=request.GET
        id=a['id']
        phoneinfo.objects.filter(id=id).delete()
        return HttpResponse('delete successful')

def baofei(request):
        a=request.GET
        id=a['id']
        phoneinfo.objects.filter(id=id).update(baofei=0)
        return HttpResponse('baofei successful')

def upfile_index(request):
	return render_to_response('upfile_index.html')
