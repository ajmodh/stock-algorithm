# Weighted Averafe For Close values
def weighted_average(list):
  return sum([list[len(list)-1 - index] * ((len(list)) - index) for index in range(len(list))])/ sum(range(len(list)+1))

# Weighted Moving Average for close value
def moving_weihted_averge(list, days):
    return [ weighted_average(list[i - (days - 1):i + 1]) if i >= days-1 else None for i in range(len(list))]
