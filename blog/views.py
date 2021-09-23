from rest_framework import generics, mixins
from .models import Blog
from .serializers import BlogSerializer



class BlogViews(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BlogSerializer

    def get_queryset(self):
        client_id = self.request.data.get("client_id") or self.request.GET.get("client_id")
        queryset = Blog.objects.all()
        if client_id:
            queryset = Blog.objects.filter(client_id=client_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

   

