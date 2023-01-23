#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < my_list:
        return None
    if idx > my_list:
        return None
    
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
