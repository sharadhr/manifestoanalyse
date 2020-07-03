import re as r
import pandas as pd
import matplotlib.pyplot as plt
import nltk

lemmatizer = nltk.stem.WordNetLemmatizer()


# CC coordinating conjunction
# CD cardinal digit
# DT determiner
# EX existential there(like: “there is” … think of it like “there exists”)
# FW foreign word
# IN preposition/subordinating conjunction
# JJ adjective ‘big’
# JJR adjective, comparative ‘bigger’
# JJS adjective, superlative ‘biggest’
# LS list marker 1)
# MD modal could, will
# NN noun, singular ‘desk’
# NNS noun plural ‘desks’
# NNP proper noun, singular ‘Harrison’
# NNPS proper noun, plural ‘Americans’
# PDT predeterminer ‘all the kids’
# POS possessive ending parent’s
# PRP personal pronoun I, he, she
# PRP$ possessive pronoun my, his, hers
# RB adverb very, silently,
# RBR adverb, comparative better
# RBS adverb, superlative best
# RP particle give up
# TO, to go ‘to’ the store.
# UH interjection, errrrrrrrm
# VB verb, base form take
# VBD verb, past tense took
# VBG verb, gerund/present participle taking
# VBN verb, past participle taken
# VBP verb, sing. present, non-3d take
# VBZ verb, 3rd person sing. present takes
# WDT wh-determiner which
# WP wh-pronoun who, what
# WP$ possessive wh-pronoun whose
# WRB wh-abverb where, when

#
def get_wordnet_pos(words):
    word_dict = {}
    id_list = ["C", "D", "E", "F", "I", "J", "L", "M", "N", "P", "R", "T", "U", "V", "W"]
    description_list = ["Conjunction or Digit", "Determiner", "Existential there", "Foreign word",
    "Preposition", "Adjective", "List marker", "Modal Noun", "Noun", "Pronoun", "Adverb", "To",
    "Interjection", "Verb", "WH words"]
    for i in description_list:
        word_dict[i] = []
    for i in words:
        for j in range(0,len(id_list)):
            if i.get_type_s == id_list[j]:
                word_dict[description_list[j]].append(i)
    return word_dict

class Word:
    def __init__(self, word):
        self.word = word
        self.wordtype = None
        #self.word = word[0]
        #self.type_l = word[1]
        #self.type_s = word[1][0]

    def word_add(self, d, s): #d is dictionary of all words. s is list of words and word type
        check = False
        text = self.word
        for i in range(0, len(s[0])):
            current_data = s[0][i]
            if text in current_data:
                current_data[text] += 1
                self.type = s[1][i]
                check = True
        if text not in s[0] and check == False:
            if text in d:
                d[text] += 1
            else:
                d[text] = 1

    def get_type_s(self):
        return self.type_s

    def get_type_l(self):
        return self.type_l


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
    prep_list = ["in", "on", "at", "for", "by", "from", "with", "to", "about", "below", "over", "above", "of", "after"]
    for i in prep_list:
        d[i] = 0
    return d

def conjunctiongen():
    d = {}
    con_list = ["and", "neither", "nor", "but", "either", "or", "yet", "so", "not only", "whether", "when"]
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
    "retrenched", "budget", "national", "government", "pap", "nsp", "wp", "psp", "sdp", "spp"]
    for i in keyword:
        d[i] = 0
    return d

def read_textfile(file_name):
    text_file = open(file_name, "r")
    text = text_file.read()
    text_file.close()
    
    return nltk.pos_tag(nltk.word_tokenize(text))

def sorter(sorted_text, d, s):
    text_obj = []
    for i in sorted_text:
        current_obj = Word(lemmatizer.lemmatize(i, "v"))
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

    file_name = "nsp.txt"
    sorted_text = read_textfile(file_name)
    word_obj = sorter(sorted_text, total_words, [worddatabase, wordassignment])
    worddatabase.append(total_words)
    data_frames = d_arrange(worddatabase)
    # for i in data_frames:
    #     # ax = i.plot.bar(x = "Words", y = "Frequency")
    #     #plt.show()
    #     # print(i, "\n")

main()
