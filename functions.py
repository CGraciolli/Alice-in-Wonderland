from functools import reduce
from stop_words import stop_words_set
import matplotlib.pyplot as plt
import seaborn as sns


def remove_stop_words(tokenized):
    """
    recives set of stop words
    and a tokenized text
    returns the tokenized text without stop words
    """

    return list(filter(lambda x : x not in stop_words_set, tokenized))


def remove_non_alphabetical(token):
    """
    recives a string in lower case
    removes all the symbols that are not letters
    """
    alph = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for symbol in token:
        if symbol in alph:
            ans += symbol
    return ans

def normalize(tokenized):
    """
    recives a tokenized list
    converts all the symbols to lower case,
    removes the stop words,
    removes punctuanion
    and removes suffixes
    """
    tok_lower = list(map(lambda x : x.lower(), tokenized))
    no_suf = list(map(lambda x : remove_non_alphabetical(x), tok_lower))
    no_empty = list(filter(lambda x : x != "", no_suf))
    no_stop = remove_stop_words(no_empty)
    return no_stop

def count_words(tokenized):
    """
    recives a list of words
    retuns the frequency dictionary
    """
    dict_freq = {}
    for word in tokenized:
        if word in dict_freq:
            dict_freq[word] += 1
        else:
            dict_freq[word] = 1
    return dict_freq

def word_probability(dic):
    """
    recives a frequency dictionary
    returns a new dictionary whose values are the word probability in percentage and rounded
    if it is greater then 0.3
    """
    total = sum(list(dic.values()))
    dic_prob = dict(map(lambda x : (x, dic[x]*100/total), dic.keys()))
    ##could be a filter
    dic_prob_pos = {}
    for key in dic_prob:
        if dic_prob[key] > 0.3:
            dic_prob_pos[key] = dic_prob[key]
    return dic_prob_pos

def display_histogram_prob(tokenized):
    """
    recives a list of words
    prints a histogram representing the word probability
    """
    dfreq = count_words(tokenized)
    dprob = word_probability(dfreq)
    keys = list(dprob.keys())
    values = []
    for key in keys:
        values.append(dprob[key])
    hist = sns.barplot(x=keys, y=values)
    hist.set_title("Histogram of Word Probability", fontsize=40)
    hist.set_ylabel("probabilities (in percentage)",fontsize=25)
    plt.xticks(rotation=45, fontsize=15)
    plt.show()

def display_histogram_freq(tokenized):
    """
    recives a list of words
    prints a histogram representing the word how many times each word is present in the text
    shows only the top 30 words for better visualization
    """
    dfreq = count_words(tokenized)
    items = dfreq.items()
    items_sort = sorted(items, key= lambda x : x[1], reverse=True)
    items_sort = items_sort[:30]
    keys = []
    values = []
    for item in items_sort:
        keys.append(item[0])
        values.append(item[1])
    hist = sns.barplot(x=keys, y=values)
    hist.set_title("Histogram of Word Frequency", fontsize=40)
    hist.set_ylabel("frequency",fontsize=25)
    plt.xticks(rotation=45, fontsize=15)
    plt.show()
    

