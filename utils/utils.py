def list_of_tuple_to_list_of_lists(tupple_list):
    list_of_lists = []
    for tupple in tupple_list:
        new_list = list(tupple)
        list_of_lists.append(new_list)
        
    return list_of_lists


