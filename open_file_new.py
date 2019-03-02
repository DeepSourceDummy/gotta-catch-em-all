import os
import this

def open_new_file_ctx(filename):
    """This will open a new file."""
    with open(filename, 'r') as file_desc:
        return file_desc.read()

def open_new_file(filename):
    """This will open a new file."""
    file_desc = open(filename, 'r')
    return file_desc.read()

a = open("data_class_test.py", 'r')
