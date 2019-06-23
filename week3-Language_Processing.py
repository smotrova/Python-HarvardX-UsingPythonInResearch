# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:30:48 2018

@author: Olena

Week 3 Language Processing

1. Read text from file
2. Count words, words statistic
3. Navigate file directories and read in multiple files/books at once

"""
text = "We appreciate your interest in our Master's program in Information Systems!"

def count_words(text):
    
    """
    Count words in a given text. Skip punctuation. Returns dictionary{word:count}
    """
    
    import string
    
    text = text.lower()
    skips = string.punctuation
    
    for symbol in skips:
        text = text.replace(symbol, "")
    
    word_count = {}
    
    for word in text.split(" "):
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

print(text)
count_words(text)  

#----------------------------------------------------

def count_words_fast(text):
    
    """
    Count words in a given text. Skip punctuation. Returns dictionary{word:count}
    
    Use function Counter from a collection
    
    """
    
    import string
    from collections import Counter
    
    text = text.lower()
    skips = string.punctuation
    
    for symbol in skips:
        text = text.replace(symbol, "")
    
    word_count = Counter(text.split(" "))
    
    return word_count

#-------------------------------------------------------------------
    
def read_book (title_path):
    
    """ Read book and return it as a string """
    
    with open(title_path, "r", encoding = "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
        
    return text
        
#----------------------------------------------------------------------

def word_stats(word_counts):
    """
    input: dictionary with words and theis frequencies
    return number of unique words and word frequencies
    
    """
    # number of uniqe words
    num_uniques = len(word_counts) 
    counts = word_counts.values()
    
    return (num_uniques, counts)
    
#------------------------------------------------------------
    
book1 = read_book ("./Data/Books/English/shakespeare/Romeo and Juliet.txt")
book2 = read_book ("./Data/Books/German/shakespeare/Romeo und Julia.txt")

(num_uniques, counts) = word_stats(count_words(book1))     
(num_uniques_de, counts_de) = word_stats(count_words(book2))  

num_uniques, sum(counts)
num_uniques_de, sum(counts_de)

#--------------------------------------------------------------

"""
how to navigate file directories and read in multiple files/books at once

"""

import os
import pandas as pd

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))

title_num = 1

book_dir = "./Data/Books"
os.listdir(book_dir)

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            # print (inputfile)
            
            text = read_book(inputfile)
            (num_unique, counts) =  word_stats(count_words_fast(text))
            
            stats.loc[title_num] = language, author.capitalize(), \
            title.replace(".txt", ""), sum(counts), num_unique
    
            title_num += 1
            
            # print("{} unique words, {} words total ".format(num_unique, sum(counts) ) )
            
stats.head()        
stats.tail()

#-----------------------------------------------------------------

"""
Plotting book statistics

"""
import matplotlib.pyplot as plt

plt.figure(figsize = (10,10))

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")

subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")

subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")

plt.legend()

plt.xlabel("Book length")
plt.ylabel("Number of unique words")

plt.savefig("length_plot.pdf")

