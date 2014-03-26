from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from atlatltest.models import Owner, House

class Command(BaseCommand):
	help="Deletes a house. Also deletes the user if the user doesn't have any other houses."
	option_list = BaseCommand.option_list + (
		make_option('--addr-contains',
		            action='store',
		            dest='address',
		            default=False,
		            help=''),
		)
	def handle(self, *args, **options):
		if options['address']:
			if House.objects.filter(address__contains=options['address']).exists():
				house=House.objects.filter(address__contains=options['address'])[0]
				self.stdout.write("Deleted house: id=[%d] address=[%s] owner=[%s]"%(house.id, house.address,house.owner.name))
				if House.objects.filter(owner=house.owner).count()==1:
					house.owner.delete()
				house.delete()
			