import sys
 
input = sys.stdin.readline
flush = sys.stdout.flush
 

a  = int(input())
b  = int(input())

if(a> 0):
    if(b > 0):
        print("1")
    else:
        print("4")
else:
    if(b>0):
        print("2")
    else:
        print("3")
