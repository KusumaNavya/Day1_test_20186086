'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
# import re
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

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def main():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    # print(tokenize(lst))
    print(word_count(str))

if __name__ == '__main__':
    main()
