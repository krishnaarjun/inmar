from rest_framework.serializers import ModelSerializer
from .models import Location,Department,Category,SubCategory,SKU
 
 
class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
 
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

class SKUSerializer(ModelSerializer):
    class Meta:
        model = SKU
        fields = "__all__"