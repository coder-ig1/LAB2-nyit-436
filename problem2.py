""" 
Author: Ezra Newman
Date: 2023-7-27
 """
""" Write a MapReduce program that only counts non-stop words. List of stopwords are: the, and,
of, a, to, in, is, it.
Example Input:
This is a sample input text. It contains some common words such as the, and, of, a, and to.
These stopwords should be removed in the output.
Example Output:
"common" 1
"contains" 1
"input" 1
"output" 1
"removed" 1
"sample" 1
"should" 1
"some" 1
"stopwords" 1
"text" 1 """
import regex as re
def main():
    read_file = open("problem2-input.txt", "r")
    reduce(map(read_file))
    return 

def map(file):
    tuple_list = []
    #create key value pairs from the input
    #key = word
    #value = 1
    file = file.read()
    file = re.split(r'[-[\]{{}}()*+?.,\\^$|#\s]+', file)
    
    stopwords = {"the", "and", "of", "a", "to", "in", "is", "it"}
    for word in file:
        #add the word to the tuple list if it is not a stop word
        if not re.match("[-[\]{{}}()*+?.,\\^$|#\s]", word) and word != "" and word.lower() not in stopwords:
            tuple_list.append({word : 1})
    
    return tuple_list
def reduce(tuple_list):
    #create a dictionary with the key being the word and the value being the count
    #if the key is already in the dictionary, increase the count
    #if the key is not in the dictionary, add the key and set the count to 1
    word_count = {}
    for tuple in tuple_list:
        for key in tuple:
            if key in word_count:
                word_count[key] += 1
            else:
                word_count[key] = 1
    
    return word_count

main()