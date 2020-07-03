class Word:
    def __init__(self, word):
        self.word = word
        self.wordtype = None

    def word_add(self, text, d, s): #d is dictionary of all words. s is list of words and word type
        if text in d:
            d[text] += 1
        else:
            d[text] = 1
        for i in range(0, len(s)):
            current_data = s[0][i]
            if text in current_data:
                current_data[text] += 1
                self.type = s[1][i]
    
    def showtype(self):
        return self.type
    