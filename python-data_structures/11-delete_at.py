#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list and idx <= len(my_list) - 1 and idx >= 0:
        my_list.remove(my_list[idx])
        return my_list
    return my_list
