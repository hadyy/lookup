from django.db import models

class Address(models.Model):
	city = models.CharField(max_length=256)

	def __unicode__(self):
		return u'%s' % (self.city)

class Category(models.Model):
	category = models.CharField(max_length=60)

	def __unicode__(self):
		return u'%s' % (self.category)

class Tag(models.Model):
	tag = models.CharField(max_length=30)

	def __unicode__(self):
		return u'%s' % (self.tag)
		
class Item(models.Model):
	name = models.CharField(max_length=256)
	slug = models.SlugField()
	category = models.ForeignKey(Category)
	visits = models.IntegerField(default=0)
	tags = models.ManyToManyField(Tag)
	show = models.BooleanField()

	def __unicode__(self):
		return u'%s' % (self.name)

class Phone(models.Model):
	number = models.IntegerField(max_length=8)
	item = models.ForeignKey(Item)
	address = models.ForeignKey(Address)

	def __unicode__(self):
		return u'%s' % (self.number)