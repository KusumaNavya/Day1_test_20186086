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
        l.append(regex.sub("",line).split())

    for s in l:
        for w in s:
            t[s] = t.get(s,0) + 1
    return t

def main():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    print(tokenize(lst))

if __name__ == '__main__':
    main()
