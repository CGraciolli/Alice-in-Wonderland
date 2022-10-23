from nltk.tokenize import word_tokenize

stop_words = open("english.txt", "r", encoding="utf8")
text_stop = stop_words.read()
stop_words.close()

stop_words_list = word_tokenize(text_stop)
stop_words_set = set(stop_words_list)