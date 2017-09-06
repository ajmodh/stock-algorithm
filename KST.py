roc_1, roc_2, roc_3, roc_4, sma_roc_1, sma_roc_2, sma_roc_3, sma_roc_4, kst = [], [], [], [], [], [], [], [], []

def sma_of_it (days, from_list):
    to_list, index, index_for_roc, total, start_index, average_per_index= [], 0,0, 0, 0,0
    for value in from_list:
        if value == "none" :
            to_list.append("none")
            start_index += 1
        else:
            if index_for_roc < days-1:
                to_list.append("none")
                index_for_roc += 1
            else:
                total = sum(from_list[start_index : index +1])
                average_per_index = total/days
                to_list.append(average_per_index)
                start_index += 1
        index += 1
    return to_list

def roc_of_it(days, from_list):
    index = 0
    to_list = []
    index_from = 0
    index_to = 0
    roc_perticular_index = 0
    for value in from_list:
        if index == len(from_list):
            break
        if index < days-1:
            to_list.insert(index,"none")
        else:
            index_from, index_to = ((index+1)-days), index
            roc_perticular_index = (((from_list[index_to] - from_list[index_from]) / from_list[index_from]) * 100)
            to_list.insert(index,roc_perticular_index)
        index += 1
    return to_list


def kst_of_it(sma1,sma2,sma3,sma4):
    kst, kst_of_index,index = [], 0, 0
    for value in sma4:
          if value == "none":
               kst.append("none")
               index +=1
          else:
              kst_of_index = sma1[index] + (sma2[index]*2)  + (sma3[index]*3) + (sma4[index]*4)
              kst.append(kst_of_index)
              index +=1
    return kst

def kst_of_list(from_list,roc_period_1,roc_period_2,roc_period_3,roc_period_4,sma_period_1,sma_period_2,sma_period_3,sma_period_4):
    roc_1 = roc_of_it(roc_period_1,from_list)
    roc_2 = roc_of_it(roc_period_2,from_list)
    roc_3 = roc_of_it(roc_period_3,from_list)
    roc_4 = roc_of_it(roc_period_4,from_list)
    sma_roc_1 = sma_of_it(sma_period_1,roc_1)
    sma_roc_2 = sma_of_it(sma_period_2,roc_2)
    sma_roc_3 = sma_of_it(sma_period_3,roc_3)
    sma_roc_4 = sma_of_it(sma_period_4,roc_4)
    return kst_of_it(sma_roc_1,sma_roc_2,sma_roc_3,sma_roc_4)

def moving_average(data, n):
    length = len(data)
    start_index = 0
    result = [None for x in range(n)]
    for index in range(n, length):
        total = sum(data[start_index:index])
        start_index += 1
        result.append(total/n)
    return result

