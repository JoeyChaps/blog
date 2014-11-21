from django.db import models
from django.conf import settings
import os.path

# Create your models here.

class Entry(models.Model):
	entry_text = models.TextField('body')
	entry_head = models.CharField('heading', max_length=100)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return '%s - "%s ..."' % (self.entry_head, self.entry_text[:10])

	def text_start(self):
		return '%s ...' % self.entry_text[:20]

	text_start.short_description = 'Body'

class Picture(models.Model):
	entry = models.ForeignKey(Entry)
	picture = models.ImageField(upload_to=settings.MEDIA_ROOT)
	caption = models.CharField(max_length=200)
	credit = models.CharField(max_length=100)
	pic_date = models.DateTimeField('date')

	def __unicode__(self):
		return self.caption

	def get_credit(self):
		return self.credit

	def get_image_filename(self):
		return os.path.basename(self.picture.url)

class Category(models.Model):
	entry = models.ForeignKey(Entry)
	cat_text = models.CharField('category', max_length=100)

	def __unicode__(self):
		return self.cat_text