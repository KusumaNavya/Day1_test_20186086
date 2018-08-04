"""Given a  number int_input, find the product of all the digits"""
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
N = int(input())
RES = 1
A = 0
while N != 0:
    A = N%10
    RES = RES*A
    N = N//10
print(RES)
if __name__ == "__main__":
    main()
