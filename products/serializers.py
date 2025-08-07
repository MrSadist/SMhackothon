from rest_framework import serializers
from  .models import Product, Category, Video, Image


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video']
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    video = VideoSerializer(many=True, read_only=True, required=False)
    image = ImageSerializer(many=True, read_only=True, required=False)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source='category',
        write_only = True
    )
    
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'total', 'category', 'category_id', 'video', 'image']
        
        def create(self, validted_data):
            videos_data = validted_data.pop('video', [])
            images_data = validted_data.pop('video', [])
            product = Product.objects.create(**validted_data)
            
            for video_data in videos_data:
                Video.objects.create(product=product, **video_data)
                
            for image_data in images_data:
                Image.objects.create(product=product, **image_data)
                
                return product
            
        
    