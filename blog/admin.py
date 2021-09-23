from django.contrib import admin
from django.contrib.postgres.fields.array import ArrayField
from django.db.models.query import QuerySet
from blog.models import Blog
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.utils.myWidgets import Select2TagWidgetArray
admin.site.unregister(Group)
admin.site.unregister(User)


class ArrayFieldListFilter(admin.SimpleListFilter):


    title = 'tags'
    parameter_name = 'tags'

    def lookups(self, request, model_admin):


        tags = Blog.objects.values_list("tags", flat=True)
        tags = [(kw, kw) for sublist in tags for kw in sublist if kw]
        tags = sorted(set(tags))
        return tags

    def queryset(self, request, queryset):
       

        lookup_value = self.value()  
        if lookup_value:
            queryset = queryset.filter(tags__contains=[lookup_value])
        return queryset



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = (ArrayFieldListFilter, )
    formfield_overrides = {
        ArrayField: {'widget': Select2TagWidgetArray(attrs={'data-placeholder': 'Please choose tags for blog','data-width': '100%', 'data-token-separators': ','})},
    }
    





