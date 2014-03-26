from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from atlatltest.models import Owner, House

class Command(BaseCommand):
	help="Allows the user to modify the address and/or owner"
	option_list = BaseCommand.option_list + (
		make_option('--id',
		            action='store',
		            dest='id',
		            default=False,
		            help=''),
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
		if options['id']:
			house=House.objects.get(id=options['id'])
			if options['address']:
				house.address=options['address']
			if options['owner']:
				if Owner.objects.filter(name=options['owner']).exists():
					owner=Owner.objects.filter(name=options['owner'])[0]
				else:
					owner=Owner(name=options['owner'])
					owner.save()
				house.owner=owner
			house.save()
			self.stdout.write("Modified house: id=[%d] address=[%s] owner=[%s]"%(house.id,house.address,house.owner.name))