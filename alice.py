from functions import normalize, display_histogram_prob, display_histogram_freq
from nltk.tokenize import wordpunct_tokenize

alice = open("alice.txt", "r", encoding="utf8")
text_alice = alice.read()
alice.close()

alice_tok = wordpunct_tokenize(text_alice)
alice_norm = normalize(alice_tok)
display_histogram_freq(alice_norm)
display_histogram_prob(alice_norm)


