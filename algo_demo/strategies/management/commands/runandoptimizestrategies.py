import math

import pybacktest as pb

from django.core.management.base import BaseCommand, CommandError

from strategies import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        #models.Run.objects.all().delete()
        for stock in models.Stock.objects.all():
            ohlc = pb.load_from_yahoo(stock.symbol + '.ns',
                                      adjust_close=True,
                                      start='2005')
            for name, strategy in models.strategies.items():
                params = {}
                for param, value in strategy['default_params'].items():
                    params[param] = (math.floor(0.75*value), math.ceil(1.25*value), 1)
                optimizer = pb.Optimizer(strategy['strategy'],
                                         ohlc,
                                         params,
                                         metrics=['profit',
                                                  'pf',
                                                  'average',
                                                  'average_gain',
                                                  'average_loss',
                                                  'winrate',
                                                  'payoff',
                                                  'pf',
                                                  'maxdd',
                                                  'rf',
                                                  'trades'],
                                         processes=1)
                for run in optimizer.results.to_dict('records'):
                    models.Run.objects.create(
                        stock = stock,
                        strategy = name,
                        profit = run.pop('profit'),
                        profit_factor = run.pop('pf'),
                        average = run.pop('average'),
                        average_gain = run.pop('average_gain'),
                        average_loss = run.pop('average_loss'),
                        winrate = run.pop('winrate'),
                        payoff = run.pop('payoff'),
                        max_drawdown = run.pop('maxdd'),
                        risk_factor = run.pop('rf'),
                        trades = run.pop('trades'),
                        params = run,
                        default = run == strategy['default_params'])
 
            
