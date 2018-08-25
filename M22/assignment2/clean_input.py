'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    regex = re.compile("[^a-b][^0-9]")
    return regex.sub("",string)
    l = []
	for _ in range(regex):
		l.append(input().split())
		
def main():
	

    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
