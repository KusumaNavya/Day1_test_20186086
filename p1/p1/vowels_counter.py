#Assume s is a string of lower case characters.
#Number of vowels: 5
"""number of vowels"""
def main():
    """find number of vowels"""
    s_v = input()
    c_v = 0
    for char in s_v:
        if char in "AEIOUaeiou":
            c_v += 1
    print("Number of vowels are:"+str(c_v))
if __name__ == "__main__":
    main()
