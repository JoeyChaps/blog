from django.contrib import admin
from blogs.models import Entry, Picture, Category

# Register your models here.
class PictureInLine(admin.TabularInline):
	model = Picture
	extra = 0

class CategoryInLine(admin.TabularInline):
	model = Category
	extra = 0

class EntryAdmin(admin.ModelAdmin):
	# fields = ['post_head', 'post_text', 'pub_date']
	fieldsets = [
		(None, 		{'fields': ['entry_head']}),
		(None,		{'fields': ['entry_text']}),
		(None, 		{'fields': ['pub_date']}),
	]
	inlines = [PictureInLine, CategoryInLine]
	list_display = ('entry_head', 'text_start', 'pub_date')
	list_filter = ('category__cat_text', 'pub_date')
	search_fields = ['entry_head']

admin.site.register(Entry, EntryAdmin)