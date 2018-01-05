from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)  # 设置多对多字段界面优化
    fieldsets = (
        ("基本信息", {'fields': ['title', 'author', 'created_time', 'modified_time']}),
        ("内容", {'fields': ['body', 'excerpt']}),
        ("关联", {'fields': ['category', 'tags']})
    )
    readonly_fields = ('created_time', 'modified_time',)  # 只读的字段


admin.site.register(Tag)
admin.site.register(Category)
# admin.site.register(Post)

admin.site.site_header = '博客运维资源管理系统'
admin.site.site_title = 'zero 的博客'


