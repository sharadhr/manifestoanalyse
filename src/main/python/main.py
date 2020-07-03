import re as r
import pandas as pd
import main.python.word as Word

def pronoungen():
    d = {}
    pronoun_list = ["i", "me", "mine", "myself", 
    "you", "your", "yourself", 
    "he", "him", "his", "himself", 
    "she", "her", "hers", "herself",
    "it", "its", "it's", "itself",
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
    keyword = ["productivity", "w", "enterprise", "gdp", "economy",
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
    sorted_text = r.split("\W+", text)
    return sorted_text

def sorter(sorted_text, d, s):
    text_obj = []
    for i in sorted_text:
        current_obj = Word(i)
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
    name = input("enter file name: ")
    sorted_text = textfile(name)
    word_obj = sorter(sorted_text, total_words, [worddatabase, wordassignment])
    data_frames = d_arrange(worddatabase.append(total_words))
    for i in data_frames:
        ax = i.plot.bar(x = "Words", y = "Frequency")

main()