import sys
from colorama import Fore, Style, init as init_colorama

init_colorama()


class DashbirdsCli:

    def __init__(self):
        self.params = [
            '-de',
            '-help'
        ]


def check_params():
    dsb = DashbirdsCli()
    
    if sys.argv[1] in dsb.params:
        print('HASUHAUSHUAHSU')
    else:
        print('não está')


if __name__ == '__main__':
    print('cli_methods.py')