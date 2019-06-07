from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.conf.urls import include, url


from .views import LocationViewSet,DepartmentViewSet,CategoryViewSet,SubCategoryViewSet,SKUViewSet

router = DefaultRouter()

#Location router
router.register(r'location', LocationViewSet, base_name='location')

# Department Router
department_router = routers.NestedSimpleRouter(router, r'location', lookup='location')
department_router.register(r'department', DepartmentViewSet,base_name='department')

# Category Router
category_router = routers.NestedSimpleRouter(department_router, r'department', lookup='department')
category_router.register(r'category', CategoryViewSet,base_name='category')

# SubCategory Router
subcategory_router = routers.NestedSimpleRouter(category_router, r'category', lookup='category')
subcategory_router.register(r'subcategory', SubCategoryViewSet,base_name='subcategory')

# SKU Router
sku_router = routers.NestedSimpleRouter(subcategory_router, r'subcategory', lookup='subcategory')
sku_router.register(r'sku', SKUViewSet,base_name='sku')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(department_router.urls)),
    url(r'', include(category_router.urls)),
    url(r'', include(subcategory_router.urls)),    
    url(r'', include(sku_router.urls)),           
]