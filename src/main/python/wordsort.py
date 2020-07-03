class Word:
    def __init__(self, word):
        self.word = word
        self.worddatabase = [__pronoungen(), __prepositiongen(), __conjunctiongen(), __quantifergen(), __articlegen(), __keywordgen()]
        self.wordassignment = ["pronoun", "preposition", "conjunction", "quantifier", "article", "keyword"]
    
    def __pronoungen(self):
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
        self.pronouns = d

    def __prepositiongen(self):
        d = {}
        prep_list = ["in", "on", "at", "for", "by", "from", "with", "to", "about", "below", "over", "above"]
        for i in prep_list:
            d[i] = 0
        self.prepositions = d

    def __conjunctiongen(self):
        d = {}
        con_list = ["and", "neither", "nor", "but", "either", "or", "yet", "so", "not only", "whether"]
        for i in con_list:
            d[i] = 0
        self.conjunctions = d

    def __quantifergen(self):
        d = {}
        quant = ["many", "few", "some", "every", "a lot", "any", "less", "fewer"]
        for i in quant:
            d[i] = 0
        self.quantifiers = d

    def __articlegen(self):
        d = {} 
        article = ["a", "an", "the", "whose", "all"]
        for i in article:
            d[i] = 0
        self.articles = d
    
    def __keywordgen(self):
        d = {}
        keyword = ["productivity", "w", "enterprise", "gdp", "economy",
        "mobility", "pmet", "jobs", "minimum wage", "cpf", "local", "singaporeans",
        "elderly", "eldercare", "poverty", "income", "tradeoff", "deficit",
        "stimulus", "invest", "investment", "invested", "population",
        "privelege", "mandate", "scheme", "monopoly", "retrenchment", 
        "retrenched", "budget"]
        for i in keyword:
            d[i] = 0
        self.keywords = d


    def word_add(self, text):
        d = {} #dictionary of all words
        if text in d:
            d[text] += 1
        else:
            d[text] = 1
        for i in range(0, len(self.worddatabase)):
            current_data = self.worddatabase[i]
            if text in current_data:
                current_data[text] += 1
                self.type = self.wordassignment[i] 
    
