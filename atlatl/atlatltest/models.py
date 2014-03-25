from django.db import models
import datetime

class Owner(models.Model):
	name=models.TextField()
	date_created=models.DateTimeField(default=datetime.datetime.now())

	def __unicode__(self):
		return u'%s' %(self.name)

class House(models.Model):
    address=models.TextField()
    owner=models.ForeignKey(Owner,related_name="owner")
    date_created=models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
		return u'%s' %(self.address)