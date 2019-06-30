from django.db import models

class Users(models.Model):
    uniqueuserid = models.CharField(max_length=20);
    name = models.CharField(max_length=30);
    password = models.CharField(max_length=20);
    photo = models.ImageField(upload_to='images', blank=True);
    dob = models.CharField(max_length=10);
    village = models.CharField(max_length=20);
    businesscat = models.CharField(max_length=20);
    businesstype = models.CharField(max_length=20);
    subsurname = models.CharField(max_length=20);
    activestatus = models.CharField(max_length=2);
        
    def __str__(self):
        return self.uniqueuserid;
 
class Villages(models.Model):
    villagename = models.CharField(max_length=30, default="")
    
class Gotra(models.Model):
    gotraname = models.CharField(max_length=30, default="")
    
class BusinessType(models.Model):
    business_name = models.CharField(max_length=30, default="")
    businesscatid = models.CharField(max_length=3, default="")
       
class BusinessCategory(models.Model):
    businesscategory = models.CharField(max_length=30, default="")  
    
class FamilyTree(models.Model):
    parentid = models.CharField(max_length=20)
    childid = models.CharField(max_length=20)   
    relation = models.CharField(max_length=10, default="")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    