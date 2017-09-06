import csv
from django.core.management.base import BaseCommand, CommandError

from strategies.models import Stock, Industry

class Command(BaseCommand):
    help = 'Load all the stocks of nifty from a file'
    source_file_path = 'ind_niftylist.csv'

    def stocks(self):
        with open(self.source_file_path) as csvfile:
            return list(csv.DictReader(csvfile))

    def get_industry(self, industry_name):
        industry, created = Industry.objects.get_or_create(name=industry_name)
        return industry
        
                
    def handle(self, *args, **options):

        for stock in self.stocks():
            _stock = Stock(name = stock['Company Name'],
                           industry = self.get_industry(stock['Industry']),
                           symbol = stock['Symbol'],
                           isin = stock['ISIN Code'])
            _stock.save()
            
        
