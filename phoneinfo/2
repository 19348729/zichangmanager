from django.db import models

# Create your models here.

class phoneinfo(models.Model):
	numbers=models.CharField(max_length=30)
	mingcheng=models.CharField(max_length=30)
	pinpai=models.CharField(max_length=30,null=True)
	xinghao=models.CharField(max_length=50,null=True)
	chicun=models.CharField(max_length=100,null=True)
	banbeninfo=models.CharField(max_length=100,null=True)
	peijian=models.CharField(max_length=100,null=True)
	zhishi=models.CharField(max_length=100,null=True)
	bianhao=models.CharField(max_length=30,null=True)
	curuser=models.CharField(max_length=30,null=True)
	bumen=models.CharField(max_length=30,null=True)
	beizhu=models.CharField(max_length=30,null=True)
	baofei=models.CharField(max_length=1,default='1')
	class Meta:
		db_table = 'phoneinfo'
	def __unicode__(self):
		return self.numbers



class phone_change_info(models.Model):
	numbers=models.CharField(max_length=50)
	olduser=models.CharField(max_length=50,null=True)
	newuser=models.CharField(max_length=50)
	createtime=models.DateTimeField()
	committime=models.DateTimeField(null=True)
	other1=models.CharField(max_length=100,null=True,blank=True)
	other2=models.CharField(max_length=100,null=True,blank=True)
	class Meta:
		db_table = 'phone_change_info'
		ordering = ['-committime']
	def __unicode__(self):
		return self.numbers
	
