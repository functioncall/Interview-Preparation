import sys
from string import ascii_lowercase as al

al_rev = []

for char in al[::-1]:
    al_rev.append(char)
rev = ''.join(al_rev)

def call_me(k):
    # Base case
    if k <= 25:
        return rev[-(k+1):]
    else:
        return str(call_me(k-25))+rev

def main():
    t = int(raw_input())

    while t:
        k = int(raw_input())
        if k <= 25:
            print rev[-(k+1):]
        else:
            print call_me(k)
        t=t-1
main()


