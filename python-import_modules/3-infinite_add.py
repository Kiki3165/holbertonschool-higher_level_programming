#!/usr/bin/python3
import sys
if __name__ == "__main__":
    all = 0
    for i in range(1, len(sys.argv)):
        all = all + int(sys.argv[i])
    print(all)
