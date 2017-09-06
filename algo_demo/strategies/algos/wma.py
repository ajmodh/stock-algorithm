def weighted_moving_average(series, period):
  period_range = range(int(1), int(period + 1))
  divided = sum([(weight * series.shift(period - weight)) for weight in period_range])
  divisor = sum(period_range)
  return divided / divisor
