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

def remove_punctuation(token):
    """
    recives one word and returns it without punctuation
    """
    punc = {".", ",", ";", ":", "?", "!", "_"}
    as_list =  list(filter(lambda x : x not in punc, token))
    return reduce(lambda x, y : x + y, as_list, "")


def remove_suffix(token):
    """
    recives a string
    if there is a non-alphabetic symbol in it
    returns the first part of the string
    for example, he´s -> he
    alice´ll -> alice
    """
    alph = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for symbol in token:
        if symbol in alph:
            ans += symbol
        else:
            break
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
    no_stop = remove_stop_words(tok_lower)
    no_punc = list(map(lambda x : remove_punctuation(x), no_stop))
    no_suf = list(map(lambda x : remove_suffix(x), no_punc))
    return no_suf

def count_words(tokenized):
    """
    recives a list of words
    retuns the frequency dictionary
    """
    dict_freq = {}
    for word in tokenized:
        if word != "":
            if word in dict_freq:
                dict_freq[word] += 1
            else:
                dict_freq[word] = 1
    return dict_freq

def word_probability(dic):
    """
    recives a frequency dictionary
    returns a new dictionary whose values are the word probability in percentage and rounded
    """
    total = sum(list(dic.values()))
    dic_prob = dict(map(lambda x : (x, round(dic[x]*100/total)), dic.keys()))
    ##could be a filter
    dic_prob_pos = {}
    for key in dic_prob:
        if dic_prob[key] > 0:
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
    #hist.set(xlabel="words", ylabel="probabilities", title="Histogram of Word Probabilities")
    hist.set_title("Histogram of Word Probabilities", fontsize=40)
    hist.set_ylabel("probabilities (in percentage)",fontsize=25)
    plt.xticks(rotation=45, fontsize=15)
    plt.show()
    
    
    

