'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    regex = re.compile("[^0-9 A-Z a-z]")
    t = {}
    l = []
    for line in string:
        l.append(reg.sub('',line).split())

    for s in l:
        for w in s:
            t[s] = t.get(w,0) + 1
    return t

def main():
    n = int(imput())
    lst = []
    for _ in range(n):
        lst.append(input())
    print(tokenize(lst))

if __name__ == '__main__':
    main()
