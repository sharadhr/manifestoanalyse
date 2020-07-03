import csv as c
import re as r

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

def main():
    d = {}
    worddatabase = [pronoungen(), prepositiongen(), conjunctiongen(), quantifergen(), articlegen(), keywordgen()]
    wordassignment = ["pronoun", "preposition", "conjunction", "quantifier", "article", "keyword"]
    
