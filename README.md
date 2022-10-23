# Alice in Wonderland
A simple textual analysis of the text from "Alice in Wonderland" by Lewis Carroll.

The objetive is to analyse how many times non-stop words are present in the text of "Alice in Wonderland".

In order to do so, first we tokenize the text using NLTK.

Then we get remove all the stop-words, as well as punctuation and suffixes.

Now that the data is normalized, we create a frequency dictionary, telling us how many times each word is present in the text.

Then we create a dictionary of probabilities, telling us what is the probability of a word being picked at random from all the non-stop words from the text.

Finally, we create a histogram from this dictionary of probabilities (for better visualization, we round the probabilities and don´t show the ones that are rounded to zero).


![alice_hist](https://user-images.githubusercontent.com/112963325/197401082-445b5758-aa49-4e81-8db0-8244ec3a4a1f.png)
