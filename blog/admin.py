from django.contrib import admin
from .models import Post

# Register your models here.
class PostDB(admin.ModelAdmin):
    list_display = ('Title', 'Author', 'Created_date', 'Published_date')
    
admin.site.register(Post,PostDB)
