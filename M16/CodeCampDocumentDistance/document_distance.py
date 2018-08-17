'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def str_op(inp_str):
    '''string operations'''
    regex = re.compile('[^a-z ]')
    return [regex.sub('', eachword.strip()) for eachword in inp_str.lower().split(' ')]

def remove_stop(word_list):
    '''removing stopwords'''
    # print(word_list)
    stop_words = load_stop('stopwords.txt')
    for each_word in stop_words:
        while each_word in word_list:
            word_list.remove(each_word)
    # print(word_list)
    return word_list

def freq(word_list, ind, dic):
    '''finding the word frequency'''
    for each_wrd in word_list:
        if each_wrd != '':
            if each_wrd not in dic:
                dic[each_wrd] = [0, 0]
            dic[each_wrd][ind] += 1
    return dic


def comp_ute(dictionary):
    '''computing the similarity value'''
    numerator = sum(value[0]*value[1] for value in dictionary.values())
    denom_1 = math.sqrt(sum(value[0]**2 for value in dictionary.values()))
    denom_2 = math.sqrt(sum(value[1]**2 for value in dictionary.values()))
    # print(numerator, denom_2, denom_1)
    return numerator/(denom_1*denom_2)

def similarity(dict1, dict2):
    '''
        comp_ute the document distance as given in the PDF
    '''
    input_1 = str_op(dict1)
    input_2 = str_op(dict2)

    # print(input_2, input_1)

    input_1 = remove_stop(input_1)
    input_2 = remove_stop(input_2)

    dictionary = {}
    dictionary = freq(input_1, 0, dictionary)
    dictionary = freq(input_2, 1, dictionary)
    # print_dic(dictionary)
    return comp_ute(dictionary)

def load_stop(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as file:
        for line in file:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
