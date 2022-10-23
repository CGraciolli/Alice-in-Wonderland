from functions import normalize, display_histogram_prob
from nltk.tokenize import word_tokenize

alice = open("alice.txt", "r", encoding="utf8")
text_alice = alice.read()
alice.close()

alice_tok = word_tokenize(text_alice)
alice_norm = normalize(alice_tok)
display_histogram_prob(alice_norm)

