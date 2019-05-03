#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    else:
        pluralize = "s" if len(sys.argv) > 2 else ""
        print("{:d} argument{:s}:".format(len(sys.argv) - 1, pluralize))
    for index in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(index, sys.argv[index]))
