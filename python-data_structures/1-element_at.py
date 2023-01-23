#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < my_list:
        return None
    if idx > my_list:
        return None
    for i in my_list:
        print(f"Element at index {idx} is {my_list}")
