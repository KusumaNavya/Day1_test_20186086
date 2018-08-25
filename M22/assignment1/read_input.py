'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    line = int(input())
    l = []
    for _ in range(line):
    	l.append(input())
    for each_line in l:
    	print(each_line)


if __name__ == '__main__':
    main()
