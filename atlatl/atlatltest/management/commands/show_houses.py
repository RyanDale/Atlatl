from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from atlatltest.models import Owner, House

class Command(BaseCommand):
	help="Shows all houses in the database. Use --name to filter by houses sold by the person with that name"
	option_list = BaseCommand.option_list + (
		make_option('--owner',
		            action='store',
		            dest='owner',
		            default=False,
		            help=''),
		make_option('--addr-contains',
		            action='store',
		            dest='address',
		            default=False,
		            help=''),
		)
	def handle(self, *args, **options):
		houses=House.objects.all()
		if options['owner']:
			houses=houses.filter(owner__name=options['owner'])
		if options['address']:
			houses=houses.filter(address__contains=options['address'])
		for house in houses:
			self.stdout.write("id=[%d] address=[%s] owner=[%s]"%(house.id, house.address,house.owner.name))