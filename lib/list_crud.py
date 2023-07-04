def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(a_list, element):
    a_list.append(element)
    return a_list

def add_element_to_start_of_list(a_list, element):
    a_list.insert(0, element)
    return a_list

def remove_element_from_end_of_list(a_list):
    a_list.pop()
    return a_list

def remove_element_from_start_of_list(a_list):
    del a_list[0]
    return a_list

def retrieve_first_element_from_list(a_list):
    return a_list[0]

def retrieve_element_from_index(a_list, index):
    return a_list[index]

def retrieve_last_element_from_list(a_list):
    return a_list[-1]
