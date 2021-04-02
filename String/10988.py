import sys
string = sys.stdin.readline()

palindrom_str = string[::-1]

if palindrom_str != string: print(0)
else: print(1)