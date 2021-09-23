from django.db.models import query
from django_select2 import forms as myforms
from blog.models import Blog

  
class Select2TagWidgetArray(myforms.Select2TagWidget):
    
    class Media:
        js = ("admin/js/vendor/jquery/jquery.min.js",)
   

    def optgroups(self, name, value, attrs=None):
        if not self.choices and value:
            self.choices = [(c, c) for c in value]
        return super().optgroups(name, value, attrs=None)

    
    def value_from_datadict(self, data, files, name):
        values = super().value_from_datadict(data, files, name)
        return ",".join(values)


