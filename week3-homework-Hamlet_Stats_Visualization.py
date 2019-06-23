# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:20:56 2018

@author: Olena

Week 3 homework 

"""


"""
In this case study, we will find and visualize summary statistics of the text 
of different translations of Hamlet. For this case study, 
functions `count_words_fast`, `read_book`, and `word_stat`s are already 
defined as in the Case 2 Videos (Videos 3.2.x).

`book_titles` is a nested dictionary, containing book titles 
within authors within languages, all of which are strings. 

"""
def books_dict():
    
    """
    return nested dictionary, containing book titles 
    within authors within languages, all of which are strings
    
    """

    import os
    
    books_dir = "./Data/Books"
    
    book_titles = {}
    for language in os.listdir(books_dir):
         
        authors = {}
        
        for author in os.listdir(books_dir + "/" + language):
            titles = []
            for title in os.listdir(books_dir + "/" + language + "/" + author):
                titles.append(title.replace(".txt", ""))
                
            authors[author] = titles
        
        book_titles[language] = authors

    return book_titles
#----------------------------------------------------------------------

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

#-----------------------------------------------------------------------  
    
book_titles = books_dict()

"""
Define hamlets as a pandas dataframe with columns language and text.

"""
import pandas as pd

hamlets = pd.DataFrame(columns = ("language", "text"))

title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = "./Data/Books/"+language+"/"+author+"/"+title+".txt"
                hamlets.loc[title_num] = language, read_book(inputfile)
                title_num += 1

#------------------------------------------------------

"""
Find the dictionary of word frequency in `text` by calling count_words_fast(). 
Store this as `counted_text`.
Create a pandas dataframe named `data`.
Using `counted_text`, define two columns in `data`:
`word`, consisting of each unique word in `text`.
`count`, consisting of the number of times each word in `word` is included in the text.
"""                
language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

"""
Add a column to `data` named `length`, defined as the length of each word.
Add another column named `frequency`, which is defined as follows for each word in data:
If count > 10, `frequency` is frequent.
If 1 < count <= 10, `frequency` is infrequent.
If count == 1, `frequency` is unique.
"""
data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10, "frequency"] = "frequent"
data.loc[(data["count"] > 1) & (data["count"] <= 10), "frequency"] = "infrequent"
data.loc[data["count"] == 1,"frequency"] = "unique"
    
# ----------------------------------------------------------------------

"""
Create a `pandas` dataframe named `sub_data` including the following columns:
`language`, which is the language of the text.
`frequency`, which is a list containing the strings "frequent", "infrequent", and "unique".
`mean_word_length`, which is the mean word length of each value in `frequency`.
`num_words`, which is the total number of words in each frequency category.

"""
def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)

# -----------------------------------------------------------------------------

"""
Join results for all translations in one table
"""
grouped_data = pd.DataFrame()

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)
    
#------------------------------------------------------------------------------

"""
Plot the word statistics of each translations on a single plot.

"""

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")

plt.show()