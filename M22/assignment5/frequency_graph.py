'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    n = list(dictionary.keys())
    n.sort()
    for key in n:
        print(str(key)+' - '+str(dictionary[key]*'#'))


def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
