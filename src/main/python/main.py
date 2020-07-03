import re as r
import pandas as pd
import matplotlib.pyplot as plt
import nltk

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


class Word:
    def __init__(self, word):
        self.word = word
        self.wordtype = None

    def word_add(self, d, s): #d is dictionary of all words. s is list of words and word type
        text = self.word
        if text not in s[0]:
            if text in d:
                d[text] += 1
            else:
                d[text] = 1
        for i in range(0, len(s[0])):
            current_data = s[0][i]
            if text in current_data:
                current_data[text] += 1
                self.type = s[1][i]
    
    def showtype(self):
        return self.type

def pronoungen():
    d = {}
    pronoun_list = ["i", "me", "mine", "myself", 
    "you", "your", "yourself", 
    "he", "him", "his", "himself", 
    "she", "her", "hers", "herself",
    "it", "its", "itself",
    "we", "ours", "us", "our", "ourselves",
    "yourselves",
    "they", "them", "their", "theirs", "theirs", "themselves"]
    for i in pronoun_list:
        d[i] = 0
    return d

def prepositiongen():
    d = {}
    prep_list = ["in", "on", "at", "for", "by", "from", "with", "to", "about", "below", "over", "above"]
    for i in prep_list:
        d[i] = 0
    return d

def conjunctiongen():
    d = {}
    con_list = ["and", "neither", "nor", "but", "either", "or", "yet", "so", "not only", "whether"]
    for i in con_list:
        d[i] = 0
    return d

def quantifergen():
    d = {}
    quant = ["many", "few", "some", "every", "a lot", "any", "less", "fewer"]
    for i in quant:
        d[i] = 0
    return d

def articlegen():
    d = {} 
    article = ["a", "an", "the", "whose", "all"]
    for i in article:
        d[i] = 0
    return d

def keywordgen():
    d = {}
    keyword = ["productivity", "enterprise", "gdp", "economy",
    "mobility", "pmet", "jobs", "minimum wage", "cpf", "local", "singaporeans",
    "elderly", "eldercare", "poverty", "income", "tradeoff", "deficit",
    "stimulus", "invest", "investment", "invested", "population",
    "privelege", "mandate", "scheme", "monopoly", "retrenchment", 
    "retrenched", "budget"]
    for i in keyword:
        d[i] = 0
    return d

def textfile(name):
    text_file = open(name, "r")
    text = text_file.read()
    text_file.close()
    sorted_text = r.split("\W+", text.lower())
    return sorted_text

def sorter(sorted_text, d, s):
    text_obj = []
    for i in sorted_text:
        current_obj = Word(lemmatizer.lemmatize(i))
        current_obj.word_add(d, s)
        text_obj.append(current_obj)
    return text_obj

def arrangexy(d):
    x = []
    y = []
    for i in d:
        x.append(i)
        y.append(d[i])
    out = pd.DataFrame({"Words":x, "Frequency": y})
    out.sort_values(by = "Frequency", ascending = False, inplace = True)
    return out

def d_arrange(l):
    out = []
    for i in l:
        out.append(arrangexy(i))
    return out

def main():
    total_words = {}
    worddatabase = [pronoungen(), prepositiongen(), conjunctiongen(), quantifergen(), articlegen(), keywordgen()]
    wordassignment = ["pronoun", "preposition", "conjunction", "quantifier", "article", "keyword"]
    name = "nsp.txt"
    sorted_text = textfile(name)
    word_obj = sorter(sorted_text, total_words, [worddatabase, wordassignment])
    worddatabase.append(total_words)
    data_frames = d_arrange(worddatabase)
    for i in data_frames:
        ax = i.plot.bar(x = "Words", y = "Frequency")
        plt.show()
        print(i, "\n")

main()
