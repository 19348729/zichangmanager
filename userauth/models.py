from django.db import models

# Create your models here.



class user(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	active=models.CharField(max_length=50)
	authlist=models.CharField(max_length=200,null=True)
	role=models.CharField(max_length=50,null=True)
	createtime=models.DateTimeField()
	other1=models.CharField(max_length=100,null=True,blank=True)
	other2=models.CharField(max_length=200,null=True,blank=True)

	
	class Meta:
		db_table = 'user'

	def __unicode__(self):
		return self.username
	
