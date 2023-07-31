""" 
Author: Ezra Newman
Date: 2023-7-27
 """
""" Let's consider a scenario where we are interested in counting the occurrences of word bigrams
instead of individual words. A word bigram refers to a pair of words that are adjacent to each
other in the text (excluding bigrams that span across line breaks). For example, given the line of
text "cat dog sheep horse," the corresponding bigrams would be ("cat", "dog"), ("dog", "sheep"),
and ("sheep", "horse"). To achieve this goal, we need to construct a map function and a reduce
function. The map function will emit each word bigram as a key-value pair, where the key
represents the bigram separated by a comma (e.g., "cat,dog"), and the value is set to 1.
Please note that we will only consider bigrams that occur on the same line, and there is no need
to handle bigrams that cross line breaks.
Here's an example illustrating the input and output format:
Example Input:
a man a plan a canal panama there was a plan to build a canal in panama in panama a canal
was built
Example Output:
"a,canal" 3
"a,man" 1
"a,plan" 2
"build,a" 1
"canal,in" 1
"canal,panama" 1
"in,panama" 2
"man,a" 1
"panama,a" 1
"plan,a" 1
"plan,to" 1
"there,was" 1
"to,build" 1
"was,a" 1
"was,built" 1 """
import regex as re

def main():
    with open("problem3-input.txt", "r") as read_file:
        reduce(map(read_file))

def map(file):
    tuple_list = []
    # Split the input into lines
    lines = file.readlines()

    # Process each line to generate word bigrams
    for line in lines:
        words = re.split(r'[-[\]{{}}()*+?.,\\^$|#\s]+', line.lower())
        if len(words) > 1:  # Check if the line has at least two words to form a bigram
            bigrams = zip(words, words[1:])  # Form word bigrams using zip
            for bigram in bigrams:
                tuple_list.append(bigram)

    print(tuple_list)
    return tuple_list

def reduce(tuple_list):
    word_count = {}
    for bigram in tuple_list:
        key = ",".join(bigram)
        if key in word_count:
            word_count[key] += 1
        else:
            word_count[key] = 1

    print(word_count)
    return word_count

main()
