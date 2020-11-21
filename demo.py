# author: Cal Schafer
# date: 2020-11-20

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [<arg2b>] [--arg3=<arg3>]

Options:
<arg1>            Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[<arg2b>]         Takes any value (this is an optional positional argument)
[--arg3=<arg3>]   Takes any value (this is an optional option)
"""

from docopt import docopt
opt = docopt(__doc__)


def main(arg, arg2, arg2b = None, arg3 = None):
    
    print(opt)
    print(type(opt))
    if arg2b != None:
        print(opt['<arg2b>'])

if __name__ == "__main__":
    main(opt["<arg1>"], opt["--arg2"], opt["<arg2b>"], opt["--arg3"])
