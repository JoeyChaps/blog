from django.contrib import admin
from blogs.models import Post, Comment, Picture, Category

# Register your models here.

class CommentInLine(admin.TabularInline):
	model = Comment
	extra = 0

class PictureInLine(admin.TabularInline):
	model = Picture
	extra = 0

class CategoryInLine(admin.TabularInline):
	model = Category
	extra = 0

class PostAdmin(admin.ModelAdmin):
	# fields = ['post_head', 'post_text', 'pub_date']
	fieldsets = [
		(None, 		{'fields': ['post_head']}),
		(None,		{'fields': ['post_text']}),
		(None, 		{'fields': ['pub_date']}),
	]
	inlines = [CommentInLine, PictureInLine, CategoryInLine]
	list_display = ('post_head', 'text_start', 'pub_date')
	list_filter = ('category__cat_text', 'pub_date')
	search_fields = ['post_head']

admin.site.register(Post, PostAdmin)