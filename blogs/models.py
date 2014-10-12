from django.db import models

# Create your models here.

class Post(models.Model):
	post_text = models.TextField('body')
	post_head = models.CharField('heading', max_length=100)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return '%s - "%s ..."' % (self.post_head, self.post_text[:10])

	def text_start(self):
		return '%s ...' % self.post_text[:20]

	text_start.short_description = 'Body'

class Picture(models.Model):
	post = models.ForeignKey(Post)
	picture = models.ImageField(upload_to='blog/%Y/%m/%d')
	caption = models.CharField(max_length=200)
	credit = models.CharField(max_length=100)
	pic_date = models.DateTimeField('date')

	def __unicode__(self):
		return self.caption

	def get_image_url(self):
		return self.image.url

class Comment(models.Model):
	post = models.ForeignKey(Post)
	com_text = models.CharField('comment', max_length=400)
	com_date = models.DateTimeField('date')

	def __unicode__(self):
		return self.com_text

class Category(models.Model):
	post = models.ForeignKey(Post)
	cat_text = models.CharField('category', max_length=100)

	def __unicode__(self):
		return self.cat_text