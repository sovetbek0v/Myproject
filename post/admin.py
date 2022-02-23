from django.contrib import admin

from applications.post.models import PostImage ,SomePost


class InlineProductImage(admin.TabularInline):
    model = PostImage
    extra = 1
    fields = ('image', )


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]


admin.site.register(SomePost, ProductAdminDisplay)
