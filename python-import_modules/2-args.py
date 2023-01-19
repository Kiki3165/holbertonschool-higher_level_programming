#!/usr/bin/python3
import sys
if __name__ == "__main__":

    argv = sys.argv[1:]

if len(argv) == 0:
    print("1 argument.")
else:
    print(f"{len(argv)} arguments {len(argv)}", end=':' if len(argv) != 1 else '.')
    print()
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")