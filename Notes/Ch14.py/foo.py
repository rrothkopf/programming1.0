import my_functions  # <== namespace
my_functions.foo()

'''
This also works (better for a large file with many functions):

from my_functions import *  <== local namespace (does not need to specify namespace)
foo()
'''


