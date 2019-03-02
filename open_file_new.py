import os
import this
import random


def open_new_file(filename):
    """This will open a new file."""
    file_desc = open(filename, 'r')
    return file_desc.read()

def open_new_file_ctx(filename):
    """This will open a new file."""
    with open(filename, 'r') as file_desc:
        return file_desc.read()

def foo_bar_baz():
    print("this should raise an issue")
    print("jfsdof fjdsklf fjsdlkc ljvsldjvld vjsdlkcvmldfks jvlkdfsjvlkdfjvlkfdjv vjdflvjdflkvlfkdvlkdf vfjvlkdfjvlkdf vjdflkvjdf")
    raise NotImplemented
