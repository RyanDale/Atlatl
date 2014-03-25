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
		)
	def handle(self, *args, **options):
		houses=House.objects.all()
		if options['owner']:
			houses=House.objects.filter(owner__name=options['owner'])
		for house in houses:
			self.stdout.write("address=[%s] owner=[%s]"%(house.address,house.owner.name))