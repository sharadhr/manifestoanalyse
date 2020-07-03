import re as r
import pandas as pd
import matplotlib.pyplot as plt
import nltk

nltk.download('tagset')
nltk.download('wordnet')
nltk.download('punkt')

lemmatizer = nltk.stem.WordNetLemmatizer()

def nltk_tagdict():
    tagdict = nltk.data.load('help/tagsets/upenn_tagset.pickle')
    tagdict.values()
    return nltk.data.load('help/tagsets/upenn_tagset.pickle')


def nltk_tags(tagdict):
    return tagdict.keys()


def nltk_tag_explanations(tagdict):
    return tagdict.values()


def get_wordnet_pos(words):
    word_dict = {}
    id_list = ["C", "D", "E", "F", "I", "J", "L",
               "M", "N", "P", "R", "T", "U", "V", "W"]
    description_list = ["Conjunction or Digit", "Determiner", "Existential there", "Foreign word",
                        "Preposition", "Adjective", "List marker", "Modal Noun", "Noun", "Pronoun", "Adverb", "To",
                        "Interjection", "Verb", "WH words"]
    for i in description_list:
        word_dict[i] = []
    for i in words:
        for j in range(0, len(id_list)):
            if i.get_type_s == id_list[j]:
                word_dict[description_list[j]].append(i)
    return word_dict


class Word:
    def __init__(self, word, id):
        self.word = word
        self.type_l = id
        self.type_s = id[0]

    def get_type_s(self):
        return self.type_s

    def get_type_l(self):
        return self.type_l

    def get_word(self):
        return self.word

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
    prep_list = ["in", "on", "at", "for", "by", "from", "with",
                 "to", "about", "below", "over", "above", "of", "after"]
    for i in prep_list:
        d[i] = 0
    return d

def conjunctiongen():
    d = {}
    con_list = ["and", "neither", "nor", "but", "either",
                "or", "yet", "so", "not only", "whether", "when"]
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

def objectifier(text):
    out = []
    for i in range(0, len(text)):
        word = text[i][0].lower
        id = text[i][1]
        out.append(Word(word, id))
    return out

def get_wordcat(words):
    word_dict = {}
    id_list = ["C", "D", "E", "F", "I", "J", "L",
               "M", "N", "P", "R", "T", "U", "V", "W"]
    description_list = ["Conjunction or Digit", "Determiner", "Existential there", "Foreign word",
                        "Preposition", "Adjective", "List marker", "Modal Noun", "Noun", "Pronoun", "Adverb", "To",
                        "Interjection", "Verb", "WH words"]
    for i in description_list:
        word_dict[i] = []
    for i in words:
        for j in range(0, len(id_list)):
            if i.get_type_s == id_list[j]:
                word_dict[description_list[j]].append(i)
    return word_dict

def get_freq(word_dicts):
    d = {}
    for i in word_dicts:
        temp = {}
        current = word_dicts[i]
        for j in current:
            if j.get_word() in temp:
                temp[j.get_word()] += 1
            else:
                temp[j.get_word()] = 1
        d[i] = temp
    return d

def arrangexy(d):
    x = []
    y = []
    for i in d:
        x.append(i)
        y.append(d[i])
    out = pd.DataFrame({"Words": x, "Frequency": y})
    out.sort_values(by="Frequency", ascending=False, inplace=True)
    return out

def main():
    #worddatabase = [pronoungen(), prepositiongen(), conjunctiongen(), quantifergen(), articlegen(), keywordgen()]
    #wordassignment = ["pronoun", "preposition", "conjunction", "quantifier", "article", "keyword"]
    file_name = "nsp.txt"
    text_tags = read_textfile(file_name) #list of tuples containing the words contained in the text document along with their NLKT ID's
    word_obj = objectifier(text_tags) #list of word objects for the words obtained from the previous step
    cat_words = get_wordcat(word_obj) #sorts the words into a dictionary with their correct categories 
    freq_words = get_freq(cat_words) #sorts the words by frequency and returns a dictionary
    data_frames = []
    for i in freq_words:
        current_dict = freq_words[i]
        data_frames.append(arrangexy(current_dict)) #creates data frames for the frequency of words and the words
    print(data_frames)
    # for i in data_frames:
    #     # ax = i.plot.bar(x = "Words", y = "Frequency")
    #     #plt.show()
    #     # print(i, "\n")


main()
