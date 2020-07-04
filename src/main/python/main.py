import pandas as pd
import matplotlib.pyplot as plt
import nltk

nltk.download('popular')
nltk.download('tagsets')
nltk.download('wordnet')

lemmatizer = nltk.stem.WordNetLemmatizer()

def nltk_tagdict():
    tagdict = nltk.data.load('help/tagsets/upenn_tagset.pickle')
    tagdict.values()
    return nltk.data.load('help/tagsets/upenn_tagset.pickle')

def nltk_tags(tagdict):
    return tagdict.keys()

def nltk_tag_explanations(tagdict):
    return tagdict.values()

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

def read_textfile(file_name):
    text_file = open(file_name, "r")
    text = text_file.read()
    text_file.close()

    return nltk.pos_tag(nltk.word_tokenize(text))

def objectifier(text):
    out = []
    for i in range(0, len(text)):
        word = text[i][0].lower()
        id = text[i][1]
        out.append(Word(word, id))
    return out

def get_wordcat(words):
    word_dict = {}
    tagdict = nltk_tagdict()
    id_list = []
    description_list = []
    for i in tagdict:
        id_list.append(i)
        description_list.append(tagdict[i])
    for i in description_list:
        word_dict[i] = []
    for i in words:
        for j in range(0, len(id_list)):
            if i.get_type_l() == id_list[j]:
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
    high = 20
    n = 0
    for i in d:
        n += 1
        x.append(i)
        y.append(d[i])
        if n == high:
            break
    out = pd.DataFrame({"Words": x, "Frequency": y})
    out.sort_values(by="Frequency", ascending=False, inplace=True)
    return out

#Add in multiparty comparison
def main():
    file_name = "nsp.txt"
    # list of tuples containing the words contained in the text document along with their NLKT ID's
    text_tags = read_textfile(file_name)
    # list of word objects for the words obtained from the previous step
    word_obj = objectifier(text_tags)
    # sorts the words into a dictionary with their correct categories
    cat_words = get_wordcat(word_obj)
    # sorts the words by frequency and returns a dictionary
    freq_words = get_freq(cat_words)
    for i in freq_words:
        current_dict = freq_words[i]
        if len(current_dict)> 0:
            # creates data frames for the frequency of words and the words
            current_data_frame = arrangexy(current_dict)
            #print(i, "\n")
            #print(current_data_frame, "\n")
            ax = current_data_frame.plot.bar(x="Words", y="Frequency", title = i[0])
            plt.show()
        else:
            continue

main()