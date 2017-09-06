from django.db import models

class Industry(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=250)
    industry = models.ForeignKey(Industry)
    symbol = models.CharField(max_length=250)
    isin = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def crossover(first, second):
    return (first > second) & (first.shift() < second.shift())

def crossunder(first, second):
    return (first < second) & (first.shift() > second.shift())
    
def sma_cross(ohlc, slow_period, fast_period):
    fast_ma = ohlc.C.rolling(fast_period).mean()
    slow_ma = ohlc.C.rolling(slow_period).mean()
    buy = cover = crossover(fast_ma, slow_ma)
    sell = short = crossunder(fast_ma, slow_ma)
    return locals()

def ema_cross(ohlc, slow_period, fast_period):
    fast_ma = ohlc.C.ewm(span=fast_period).mean()
    slow_ma = ohlc.C.ewm(span=slow_period).mean()
    buy = cover = crossover(fast_ma, slow_ma)
    sell = short = crossunder(fast_ma, slow_ma)
    return locals()

from .algos import strategies as s

strategies = {
    'SMA Cross': {
        'strategy': s.sma_cross,
        'default_params': {
            'period_small': 10,
            'period_long': 5
        }
    },

    'EMA Cross': {
        'strategy': s.ema_cross,
        'default_params': {
            'period_small': 10,
            'period_long': 5
        }
    },
    'WMA Cross': {
        'strategy': s.wma_cross,
        'default_params': {
            'period_small': 10,
            'period_long': 5
        }
    },
    'DEMA Cross': {
        'strategy': s.dema_cross,
        'default_params': {
            'period_small': 10,
            'period_long': 5
        }
    },
    'TEMA Cross': {
        'strategy': s.tema_cross,
        'default_params': {
            'period_small': 10,
            'period_long': 5
        }
    },
    
    'SuperTrend Cross': {
        'strategy': s.supertrend_cross,
        'default_params':{
            'period_small': 10,
            'multiplier': 5
        },
    },
    'RSI EMA Cross': {
        'strategy': s.rsi_cross,
        'default_params':{
            'rsi_period': 14,
            'avg_period': 9
        },
    },
    'MACD Cross': {
        'strategy': s.macd_cross,
        'default_params':{
            'small_ema': 12,
            'long_ema': 24,
            'avg_period': 9
        },
    },
    'TRIX Cross': {
        'strategy': s.trix_cross,
        'default_params':{
            'trix_period': 10,
            'avg_period': 9
        },    
    },
    'Chande Vidya': {
        'strategy': s.chandevidya,
        'default_params':{
            'period': 9
        },    
    }
}

class Run(models.Model):
    stock = models.ForeignKey(Stock)
    strategy = models.CharField(max_length=250)
    params = models.TextField()
    profit = models.FloatField(null=True)
    profit_factor = models.FloatField(null=True)
    average = models.FloatField(null=True)
    average_gain = models.FloatField(null=True)
    average_loss = models.FloatField(null=True)
    winrate = models.FloatField(null=True)
    payoff = models.FloatField(null=True)
    profit_factor = models.FloatField(null=True)
    max_drawdown = models.FloatField(null=True)
    risk_factor = models.FloatField(null=True)
    trades = models.FloatField(null=True)
    default = models.BooleanField(default=False)
    netted = models.FloatField(null=True)
    grossed = models.FloatField(null=True)
    '''
    class Meta:
        ordering = ( 'stock', 'strategy', '-profit')
    '''
