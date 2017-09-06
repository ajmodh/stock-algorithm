def change(from_list):
    change_list, current_change_value = [], 0
    for index, value in enumerate(from_list):
        if index == 0:
            change_list.append("none")
        else:
            current_change_value = value - from_list[index-1]
            change_list.append(current_change_value)
    return change_list

def gain_loss(from_list):
    gain_list, loss_list = [], []
    for value in from_list:
        if value == "none":
            gain_list.append("none")
            loss_list.append("none")
        else:
            if value > 0:
                gain_list.append(value)
                loss_list.append(0)
            else:
                gain_list.append(0)
                loss_list.append(-value)
    return gain_list, loss_list

def average_gain_loss(from_list, days):
    average_list = []
    for index, values in enumerate(from_list):
        if index < days:
            average_list.append("none")
        else:
            if index == days:
                average_list.append((sum(from_list[1:days+1]))/days)
            else:
                average_list.append (((average_list[index-1]* (days-1)) +values) /days)
    return average_list

def ralatice_strength(gain_list, loss_list):
    rs_list = []
    for index in range(len(gain_list)):
        if gain_list[index] == "none":
            rs_list.append("none")
        else:
            rs_list.append(gain_list[index]/loss_list[index])
    return rs_list

def rsi_result(avg_loss_list, rs_list):
    rsi_list = []
    for index in range(len(rs_list)):
        if rs_list[index] == "none":
            rsi_list.append("none")
        else:
            if avg_loss_list[index] == 0:
                rsi_list.append(100.0)
            else:
                rsi_list.append(100 -(100 /(1 +rs_list[index])))
    return rsi_list

def rsi_calculation(close_price, days):
    change_list, gain, loss, avg_gain, avg_loss, rs, rsi_reslt = [], [], [], [],[], [], []
    change_list = change(close_price)

    gain, loss = gain_loss(change_list)

    avg_gain = average_gain_loss(gain, days)

    avg_loss = average_gain_loss(loss, days)

    rs = ralatice_strength(avg_gain,avg_loss)

    rsi_reslt = rsi_result(avg_loss,rs)

    return change_list, gain, loss, avg_gain, avg_loss, rs, rsi_reslt