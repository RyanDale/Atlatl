from django.db import models

class Owner(models.Model):
	name=models.TextField()

	def __unicode__(self):
		return u'%s' %(self.name)

class House(models.Model):
    address=models.TextField()
    owner=models.ForeignKey(Owner,related_name="owner")
    
    def __unicode__(self):
		return u'%s' %(self.address)