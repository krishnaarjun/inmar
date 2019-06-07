from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Deleted', 'Deleted')
)

class Location(models.Model):
	name = models.CharField(help_text='Location_name',max_length=50)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')

class Department(models.Model):
	name = models.CharField(help_text='Department_name',max_length=50)
	location = models.ForeignKey(Location,on_delete=models.SET_NULL,blank=True,null=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')
	
class Category(models.Model):
	name = models.CharField(help_text='Category',max_length=50)
	department = models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')
	
class SubCategory(models.Model):
	name = models.CharField(help_text='subcategory',max_length=50)
	category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')
	
class SKU(models.Model):
	code = models.CharField(help_text='code',max_length=50)
	subcategory = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,blank=True,null=True) 
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')
	