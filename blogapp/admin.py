from django.contrib import admin
from .models import BlogPost 

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')  
    list_filter = ('pub_date',)  
    search_fields = ('title', 'content') 
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    
admin.site.register(BlogPost, BlogPostAdmin)
