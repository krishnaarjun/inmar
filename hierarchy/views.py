import json
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response
from .serializers import LocationSerializer,DepartmentSerializer,CategorySerializer,SubCategorySerializer,SKUSerializer
from .models import Location,Department,Category,SubCategory,SKU
from django.contrib.auth.models import User

# Create your views here.
class LocationViewSet(viewsets.ViewSet):
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
    	serializer = LocationSerializer(data=request.data)
    	serializer.is_valid(raise_exception=True)
    	serializer.save()
    	return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = Location.objects.get(pk=kwargs['pk'])
        serializer = LocationSerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)	

    def list(self, request,):
        queryset = Location.objects.filter()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Location.objects.filter()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

class DepartmentViewSet(viewsets.ViewSet):
    serializer_class = DepartmentSerializer
    def create(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = Department.objects.get(pk=kwargs['pk'])
        serializer = DepartmentSerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, location_pk=None):
        queryset = Department.objects.filter(location=location_pk)
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, location_pk=None):
        queryset = Department.objects.filter(pk=pk, location=location_pk)
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = Category.objects.get(pk=kwargs['pk'])
        serializer = CategorySerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, location_pk=None, department_pk=None):
        queryset = Category.objects.filter(department__location=location_pk, department=department_pk)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, location_pk=None, department_pk=None):
        queryset = Category.objects.filter(pk=pk,department__location=location_pk, department=department_pk)
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class SubCategoryViewSet(viewsets.ViewSet):
    serializer_class = SubCategorySerializer
    def create(self, request, *args, **kwargs):
        serializer = SubCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = SubCategory.objects.get(pk=kwargs['pk'])
        serializer = SubCategorySerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, location_pk=None, department_pk=None,category_pk=None):
    	queryset = SubCategory.objects.filter(category__department__location=location_pk, category__department=department_pk,category=category_pk)
    	serializer = SubCategorySerializer(queryset, many=True)
    	return Response(serializer.data)

    def retrieve(self, request, pk=None, location_pk=None, department_pk=None,category_pk=None):
    	queryset = SubCategory.objects.filter(pk=pk,category__department__location=location_pk, category__department=department_pk,category=category_pk)
    	subcategory = get_object_or_404(queryset, pk=pk)
    	serializer = SubCategorySerializer(subcategory)
    	return Response(serializer.data)


class SKUViewSet(viewsets.ModelViewSet):

    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

    def create(self, request, *args, **kwargs):
        serializer = SKUSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = SKU.objects.get(pk=kwargs['pk'])
        serializer = SKUSerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self,request,location_pk=None,department_pk=None,category_pk=None,subcategory_pk=None):
        skus = self.queryset.filter(subcategory=subcategory_pk)
        serializer = self.get_serializer(skus)
        return Response(serializer.data)

    def retrieve(self,request,pk=None,location_pk=None,department_pk=None,category_pk=None,subcategory_pk=None):
        sku = self.queryset.get(pk=pk,subcategory=subcategory_pk)
        serializer = self.get_serializer(sku)        
        return Response(serializer.data)

def skudata(request):
    # data ={
    #         "name": "Top Level",
    #         "children": [
    #           { 
    #             "name": "Level 2: A",
    #             "children": [
    #               { "name": "Son of A" },
    #               { "name": "Daughter of A" }
    #             ]
    #           },
    #           { "name": "Level 2: B" }
    #         ]
    #         }
    # import pdb;pdb.set_trace()
    links = []
    locations = Location.objects.all()
    departments = Department.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    for d in departments:
        c = d.name
        p = d.location.name
        links.append((p,c))
    for cat in categories:
        c = cat.name
        p = cat.department.name
        links.append((p,c))
    for scat in subcategories:
        c = scat.name
        p = scat.category.name
        links.append((p,c))
    # import pdb;pdb.set_trace()
    parents, children = zip(*links)
    root_nodes = {x for x in parents if x not in children}
    for node in root_nodes:
        links.append(('Root', node))

    def get_nodes(node):
        d = {}
        d['name'] = node
        children = get_children(node)
        if children:
            d['children'] = [get_nodes(child) for child in children]
        return d

    def get_children(node):
        return [x[1] for x in links if x[0] == node]

    tree = get_nodes('Root')
    return HttpResponse(json.dumps(tree, indent=4))
    # data  ={}
    # data ['name'] = 'Master Hierarchy'
    # locations = Location.objects.all()
    # for l in locations:
    #     data['children'] = 

class UserLogin(View):

    def get(self, request):
    	# import pdb;pdb.set_trace()
    	return render(request,'index.html', {})

    def post(self, request):
    	# import pdb;pdb.set_trace()
    	uname=request.POST.get('username')
    	pwd=request.POST.get('password')
    	user=authenticate(username=uname, password=pwd)
    	if user is not None:
    		login(request, user)
    		return HttpResponseRedirect('/')
    	else:
    		return render(request,'index.html', {'error':'Invalid User'})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def home(request):
    locations = Location.objects.all()
    departments = Department.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    skus = SKU.objects.all()
    return render(request,'home.html',{'locations':locations,'departments':departments,'categories':categories,'subcategories':subcategories,'skus':skus})

def addlocation(request,pk=None):
	return render(request,'location.html',{'type':'add'})
def editlocation(request,pk=None):
    if pk is not None:
        location  = Location.objects.get(pk=pk)
    else:
    	location = []	
    return render(request,'location.html',{'location':location,'type':'edit'})

def adddepartment(request):
    locations = Location.objects.all()
    return render(request,'adddepartment.html',{'locations':locations,'type':'add'})

def editdepartment(request,pk=None):
    locations = Location.objects.all()
    if pk is not None:
    	department  = Department.objects.get(pk=pk)
    else:
    	department = []
    return render(request,'adddepartment.html',{'department':department,'locations':locations,'type':'edit'})

def addcategory(request,pk=None):
	departments = Department.objects.all()
	return render(request,'addcategory.html',{'departments':departments,'type':'add'})

def editcategory(request,pk=None):
    if pk is not None:
        category  = Category.objects.get(pk=pk)
    else:
        category = []
    departments = Department.objects.all()
    return render(request,'addcategory.html',{'category':category,'departments':departments,'type':'edit'})

def addsubcategory(request,pk=None):
    categories = Category.objects.all()
    return render(request,'addsubcategory.html',{'categories':categories,'type':'add'})

def editsubcategory(request,pk=None):
    categories = Category.objects.all()
    if pk is not None:
        subcategory  = SubCategory.objects.get(pk=pk)
    else:
        subcategory = []    
    return render(request,'addsubcategory.html',{'categories':categories,'subcategory':subcategory,'type':'edit'})

def addsku(request,pk=None):
    subcategories = SubCategory.objects.all()
    return render(request,'addSKU.html',{'subcategories':subcategories,'type':'add'})

def editsku(request,pk=None):
    subcategories = SubCategory.objects.all()
    if pk is not None:
        sku  = SKU.objects.get(pk=pk)
    else:
        sku = []    
    return render(request,'addSKU.html',{'subcategories':subcategories,'sku':sku,'type':'edit'})
