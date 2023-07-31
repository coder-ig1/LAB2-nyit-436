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
    map(read_file)
    """  reduce()
    write_file """

def map(file):
    dict = {}
    #create key value pairs from the input
    #key = word
    #value = 1
    file = file.read()
    file = file.split(" ")
    print(file)
    for word in file:
        if re.match(r'\w+', word):
            dict.update( {word : 1})
    print(dict)
    return dict

main()