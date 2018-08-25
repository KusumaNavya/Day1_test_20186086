'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re

def word_count(string):
    my_string = string.lower().split()
    my_dict = {}
    for item in my_string:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    print(my_dict)

# def tokenize(string):
#     regex = re.compile("[^0-9 A-Z a-z]")
#     t = {}
#     l = []
#     for line in string:
#         l.append(regex.sub("",line).split())

#     for s in l:
#         for w in s:
#             t[s] = t.get(w,0) + 1
#     return t

def main():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    # print(tokenize(lst))
    print(word_count(string))

if __name__ == '__main__':
    main()
