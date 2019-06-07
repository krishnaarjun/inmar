"""inmar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


"""



from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path,include
from hierarchy import routes
from hierarchy.views import UserLogin,home,addlocation,editlocation,adddepartment,addcategory,addsubcategory,editdepartment,editcategory,editsubcategory,addsku,editsku,skudata,user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/',a)
    path(r'login/',UserLogin.as_view()),
    path(r'logout/',user_logout),
    path(r'',home),
    path(r'api/v1/', include(routes)),
    url(r'editlocation/(?P<pk>[0-9]*)[/]*$',editlocation),
    url(r'editdepartment/(?P<pk>[0-9]*)[/]*$',editdepartment),
    url(r'editcategory/(?P<pk>[0-9]*)[/]*$',editcategory),
    url(r'editsubcategory/(?P<pk>[0-9]*)[/]*$',editsubcategory),
    url(r'editsku/(?P<pk>[0-9]*)[/]*$',editsku),
    path(r'addlocation/',addlocation),
    path(r'adddepartment/',adddepartment),
    path(r'addcategory/',addcategory),
    path(r'addsubcategory/',addsubcategory),
    path(r'addsku/',addsku),
    path(r'skudata/',skudata),

]
