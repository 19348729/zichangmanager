from django.shortcuts import render

from zichanmanager.userauth.models import *
from zichanmanager.phoneinfo.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
# Create your views here.



#####change list
def change_info(request):
	print "nbbbbb"
	username=request.session['username']
	print "username:"
	print username
	role=user.objects.get(username=username).role
	print "role:"
	print role
	if role == 'admin':
		a=phoneinfo.objects.all()
		print "okkkkkkk"
	else:
		a=phoneinfo.objects.filter(curuser=username)
	print a
	print "nbbbbbbbbbbbbbbbbbbbbbbbb"
	print len(a)
	b=user.objects.all()
	print "bbbbbb======"
	print b
	p=phone_change_info.objects.filter(committime=None)
	k=''
	for i in p:
		print "%%%%%%%%%%%%"
		print i.numbers
		k=k+i.numbers
	print "dfdfsfsdfsa$$$$$$$$$$$$$$$$$"
	print k	
	#return render_to_response("change_index.html")
	return render_to_response("change_index.html",{'a':a,'b':b,'k':k})


####change

def phone_change_req(request):
	a=request.POST
	print "a======"
	print a
	id=a['id']
	print id
	p_info=phoneinfo.objects.get(id=id)
	print p_info
	
	numbers=p_info.numbers
	olduser=p_info.curuser
	newuser=a['user']
	mingcheng=p_info.mingcheng
	xinghao=p_info.xinghao
	print "++++++++++++++++++++++++++++++++++++"
	print olduser,newuser,numbers
	createtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	phone_change_info.objects.create(olduser=olduser,newuser=newuser,numbers=numbers,createtime=createtime,other1=mingcheng,other2=xinghao)
	return HttpResponse("ok")



def change_commit_index(request):
	username=request.session['username']
	print username
	a=phone_change_info.objects.filter(newuser=username,committime__isnull=True)

	print a
	return render_to_response("change_commit_index.html",{'a':a})

def change_commit(request):
	a=request.POST
	id=a['id']	
	p_info=phone_change_info.objects.get(id=id)
	phone_numbers=p_info.numbers
	curuser=p_info.newuser
	committime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	phone_change_info.objects.filter(id=id).update(committime=committime)
	phoneinfo.objects.filter(numbers=phone_numbers).update(curuser=curuser)
	return HttpResponse("ok")

def change_find_index(request):
	if request.GET.has_key('numbers'):
		numbers=request.GET['numbers']
		p_list=phone_change_info.objects.filter(numbers=numbers)
	else:
		p_list=[]
	return render_to_response("change_find_index.html",{'a':p_list})
