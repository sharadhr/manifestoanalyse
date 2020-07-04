import pandas as pd
import matplotlib.pyplot as plt
import nltk

#nltk.download('popular')
#nltk.download('tagsets')
#nltk.download('wordnet')

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
    text_file = open(file_name, encoding = "utf-8")
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
    high = 500
    n = 0
    for i in d:
        n += 1
        x.append(i)
        y.append(d[i])
        if n == high:
            break
    out = pd.DataFrame({"Words": x, "Frequency": y})
    out.sort_values(by="Frequency", ascending=True, inplace=True)
    return out

def convert_to_dataframe(file_name):
    text_tags = read_textfile(file_name)
    word_obj = objectifier(text_tags)
    cat_words = get_wordcat(word_obj)
    freq_words = get_freq(cat_words)
    dict_dataframe = {}
    for i in freq_words:
        current_dict = freq_words[i]
        if len(current_dict) > 0:
            current_data_frame = arrangexy(current_dict)
            dict_dataframe[i[0]] = current_data_frame
        else:
            continue
    return dict_dataframe

def sort_words(party_dict):
    adj = []
    adv = []
    pron = []
    verb = []
    noun = []
    for i in party_dict:
        current_df = party_dict[i]
        if "adjective" in i:
            adj.append(current_df)
        elif "adverb" in i:
            adv.append(current_df)
        elif "pronoun" in i:
            pron.append(current_df)
        elif "verb" in i:
            verb.append(current_df)
        elif "noun" in i:
            if "pronoun" not in i:
                noun.append(current_df)
            else:
                continue
    adj_df = pd.concat(adj)
    adv_df = pd.concat(adv)
    pron_df = pd.concat(pron)
    verb_df = pd.concat(verb)
    noun_df = pd.concat(noun)
    check = 0
    word_cat_dict = {"Adjectives": adj_df.sort_values(by="Frequency", ascending = check), 
    "Adverbs": adv_df.sort_values(by="Frequency", ascending = check), 
    "Pronouns": pron_df.sort_values(by="Frequency", ascending = check),
     "Verbs": verb_df.sort_values(by="Frequency", ascending = check), 
     "Noun": noun_df.sort_values(by="Frequency", ascending = check)
     }
    return word_cat_dict

def concatenate_cats(d):
    adj = []
    adv = []
    pron = []
    verb = []
    noun = []
    out = [adj, adv, pron, verb, noun]
    for i in d:
        current_party = d[i]
        index = 0
        for j in current_party:
            out[index].append(current_party[j])
            index += 1
    return out
    
#Add in multiparty comparison
def main():
    file_name = ["nsp.txt", "pap.txt", "psp.txt", "wp.txt", "spp.txt"]
    party_name = [["NSP"], ["PAP"], ["PSP"], ["WP"], ["SPP"]]
    all_df_list = []
    sorted_dict = {}

    for i in file_name:
        df_dict = convert_to_dataframe(i)
        all_df_list.append(df_dict)

    for i in range(0 , len(all_df_list)):
        party_dict = all_df_list[i]
        sorted_dict[party_name[i][0]] = sort_words(party_dict)
    
    #test = concatenate_cats(sorted_dict)
    for i in sorted_dict:
        current_dict = sorted_dict[i]
        for j in current_dict:
            current_df = current_dict[j]
            if len(current_df) < 15:
                ax = current_df.plot.bar(x="Words", y="Frequency", title = j + " used by "+i, fontsize = 8)
            else:
                ax = current_df[:15].plot.bar(x="Words", y="Frequency", title = j + " used by "+i, fontsize = 8)
            #ax.legend([i])
            plt.show()

main()