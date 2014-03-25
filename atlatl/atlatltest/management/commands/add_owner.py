from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from atlatltest.models import Owner, House

class Command(BaseCommand):
	help="Adds an owner to the database"
	option_list = BaseCommand.option_list + (
		make_option('--name',
		            action='store',
		            dest='name',
		            default=False,
		            help=''),
		)
	def handle(self, *args, **options):
		if options['name']:
			owner = Owner(name=options['name'])
			owner.save()
			self.stdout.write("Added owner: name=[%s]"%owner.name)