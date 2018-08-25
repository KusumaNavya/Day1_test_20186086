'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    line = int(input())
    l_l = []
    for _ in range(line):
        l_l.append(input())
    for each_line in l_l:
        print(each_line)


if __name__ == '__main__':
    main()
