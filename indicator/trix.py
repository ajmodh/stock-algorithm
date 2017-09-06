def percentage_change(tema_list):
    per_change_list, per_cange_1_list, per_change_value = [], [], 0
    for index,values in enumerate(tema_list):
        if values == "none":
            per_change_list.append("none")
            per_cange_1_list.append("none")
        else:
            if tema_list[index-1] == "none":
                per_change_list.append("none")
                per_cange_1_list.append("none")
            else:
                per_change_value = ((tema_list[index] -tema_list[index - 1])/tema_list[index -1]) *100
                per_change_list.append(per_change_value)
                per_cange_1_list.append(1 -per_change_value)
    return per_change_list, per_cange_1_list
