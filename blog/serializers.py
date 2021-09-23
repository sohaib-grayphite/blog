from rest_framework import serializers
from blog.models import Blog, Author
from easy_thumbnails.templatetags.thumbnail import thumbnail_url


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Author
        fields = "__all__"   


class BlogSerializer(serializers.ModelSerializer):
    author_name= serializers.ReadOnlyField(source='author.name')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        if instance.content:
            response['content']=instance.content.html
            response['tags']=instance.tags
            response['photo']=thumbnail_url(instance.photo, 'compressed')

            
        return response
    
    
    class Meta:

        model = Blog
        fields = ('id', 'name', 'author_name','content','photo','created_at')        
        
     
        
