from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db import models
from main_app.models import Post, Image
from .forms import PostForm


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ImagePreviewWidget(admin.widgets.AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        if value:
            file_url = value.url
            output = f'<img src="{file_url}" style="max-height: 100px; max-width: 100px;" />'
        return mark_safe(output)


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [ImageInline]
    list_display = ('title', 'author', 'created_on', 'updated_on', 'status')  # Include 'status' in list_display
    search_fields = ('title', 'author', 'content',  'status')
    list_filter = ('status',)  # Add 'status' to list_filter

    formfield_overrides = {
        models.ImageField: {'widget': ImagePreviewWidget},
    }


admin.site.register(Post, PostAdmin)
