from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from atlatltest.models import Owner, House

class Command(BaseCommand):
	help="Adds a house to the database"
	option_list = BaseCommand.option_list + (
		make_option('--address',
		            action='store',
		            dest='address',
		            default=False,
		            help=''),
		make_option('--owner',
		            action='store',
		            dest='owner',
		            default=False,
		            help=''),
		)
	def handle(self, *args, **options):
		if options['address'] and options['owner']:
			owner_name=options['owner']
			if Owner.objects.filter(name=owner_name).exists():
				owner=Owner.objects.filter(name=owner_name)[0]
			else:
				owner=Owner(name=owner_name)
				owner.save()
				self.stdout.write("Added owner: name=[%s]"%owner.name)
			house = House(address=options['address'],owner=owner)
			house.save()
			self.stdout.write("Added house: id=[%d] address=[%s] owner=[%s]"%(house.id,house.address,house.owner.name))