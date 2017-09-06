def weighted_moving_average(series, period):
  period_range = range(int(1),int (period + 1))
  divided = sum([(weight * series.shift(period - weight)) for weight in period_range])
  divisor = sum(period_range)
  return divided / divisor

# select a.*, (a.price+b.price + c.price)/3 as sma from stock_test a left join stock_test b on a.id = b.id+1 left join stock_test c on b.id+1 = c.id+2 where a.script = 'ACC' order by a.id;