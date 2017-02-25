import os

DATADIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

def welcome():
    '''Reads the welcome.txt data file, and print the output to
    stdout'''
    with open(os.path.join(DATADIR, 'welcome.txt'), 'r') as f:
        print(f.read())

