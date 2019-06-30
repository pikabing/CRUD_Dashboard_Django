from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from users.models import Users, Villages, Gotra, BusinessCategory, BusinessType, FamilyTree
from django.http import HttpResponse
import json as simplejson
from django.core.files.storage import FileSystemStorage

def userinactivelist(request):
     all_users = Users.objects.filter(activestatus = '0')  
     return render(request, "users/users_list.html", {
        'users':all_users
    })
    
def userlist(request):
    all_users = Users.objects.filter(activestatus = '1')  
    return render(request, "users/users_list.html", {
        'users':all_users
    })
    
def edituser(request, id):
    user = Users.objects.get(id = id )
    villages = Villages.objects.all()
    gotra = Gotra.objects.all()
    businesscategory = BusinessCategory.objects.all()
    id = BusinessCategory.objects.filter(businesscategory=user.businesscat).values('id')[0];
    businesstype = (BusinessType.objects.filter(businesscatid = id.get('id')))
    return render(request, "users/users_edit.html", {
        'user':user,
        'villages':villages,
        'gotra':gotra,
        'businesscategory':businesscategory,
        'businesstype':businesstype,
    })
    
def get_type(request, value):
    id = BusinessCategory.objects.filter(businesscategory=value).values('id')[0];
    business_name = list(BusinessType.objects.filter(businesscatid = id.get('id')))
    return HttpResponse(simplejson.dumps(business_name,default=lambda o: o.__dict__, 
            sort_keys=True, indent=4), content_type="application/json")

def update(request, pk): 
    user = Users.objects.get(id = pk)
    name = request.POST.get("name")
    gotra = request.POST.get("gotra")
    dob = request.POST.get("dob")
    village = request.POST.get("village")
    password = request.POST.get("password")
    bcat = request.POST.get("businesscategory")
    btype = request.POST.get("businesstype")
    image = request.POST.get('imagestring')
    if(image != ""):
        uploaded_file = request.FILES['imagestring']
        fs = FileSystemStorage()
        fs.save(image, uploaded_file)
        user.photo = uploaded_file.name
                
    user.name = name
    user.subsurname = gotra
    user.dob = dob
    user.village = village
    user.password = password
    user.businesscat = bcat
    user.businesstype = btype
    
    user.save()
    
    return redirect(reverse('users:list'))

class UserDetail(generic.DetailView):
    model = Users
    
class UserDelete(generic.DeleteView):
    model = Users
    success_url = reverse_lazy('users:list')

def makeactive(request, id):
    user = Users.objects.get(id = id )
    user.activestatus = 1
    user.save()
    return redirect(reverse('users:pending'))
       
def makeinactive(request, id):
    user = Users.objects.get(id = id )
    user.activestatus = 0
    user.save()
    return redirect(reverse('users:list'))

def addrelation(request, pk):
    user = Users.objects.get(id = pk)
    return render(request, "users/add_relation.html", {
        'user':user
    })

def get_user_auto(request):
    user_list = list(Users.objects.all())
    return HttpResponse(simplejson.dumps(user_list,default=lambda o: o.__dict__, 
            sort_keys=True, indent=4), content_type="application/json")

def user_relation(request, id):
    user = Users.objects.get(id=id)
    familytree = FamilyTree()
    familytree.parentid = user.uniqueuserid
    familytree.childid = request.POST.get('child')
    familytree.relation = request.POST.get('relation')
    familytree.save()
    
    return redirect(reverse('users:active'))


