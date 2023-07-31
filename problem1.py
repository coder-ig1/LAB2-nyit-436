""" 
Author: Ezra Newman
Date: 2023-7-27
 """
""" Write a MapReduce program that counts the number of unique words in a given text file.
Example Input:
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec condimentum elit vel mauris varius, id laoreet tortor placerat.
Nulla scelerisque felis ac risus varius, sit amet luctus elit mattis.
Example Output:
"adipiscing" 1
"condimentum" 1
"consectetur" 1
"Donec" 1
"dolor" 1
"elit" 1
"felis" 1
"id" 1
"ipsum" 1
"laoreet" 1
"luctus" 1
"mattis" 1
"mauris" 1
"Nulla" 1
"placerat" 1
"risus" 1
"scelerisque" 1
"sit" 1
"tortor" 1
"vel" 1
"varius" 1 """
import regex as re
def main():
    read_file = open("problem1-input.txt", "r")
    reduce(map(read_file))
    return 

def map(file):
    tuple_list = []
    #create key value pairs from the input
    #key = word
    #value = 1
    file = file.read()
    file = re.split(r'[-[\]{{}}()*+?.,\\^$|#\s]+', file)
    print(file)
    for word in file:
        if not re.match("[-[\]{{}}()*+?.,\\^$|#\s]", word) and word != "":
            tuple_list.append({word : 1})
    
    print(tuple_list)
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
    print(word_count)
    return word_count

main()