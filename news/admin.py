from django.contrib import admin
from news.models import Category
from news.models import News
from news.models import SocialPage
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','url','image_tag',)
    search_fields = ('title','url',)
    list_filter = ('title','url',)
    list_per_page: 12
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','date','url',)
    search_fields = ('title', 'url',)
    list_filter = ('title','url',)
    list_per_page: 12
class SocialAdmin(admin.ModelAdmin):
        list_display = ('fb', 'yt', 'twt','insta',)
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(SocialPage, SocialAdmin)
