from django.contrib import admin
from .models import Product, Category, Video, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    fields=['image']

class VideoInline(admin.TabularInline):
    model=Video
    extra = 3
    fields = ['video']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title', )
    inlines = [VideoInline, ImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video')



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')