# Alice in Wonderland
A simple textual analysis of the text from "Alice in Wonderland" by Lewis Carroll.

The objetive is to analyse how many times non-stop words are present in the text of "Alice in Wonderland".

In order to do so, first we tokenize the text using **NLTK**.

Then we get remove all the stop-words, as well as punctuation and suffixes.

Now that the data is normalized, we create a frequency dictionary, telling us how many times each non stop-word is present in the text.

Then we create a dictionary of probabilities, telling us what is the probability of a word being picked at random from all the non-stop words from the text.

Finally, we create two histograms using **Seaborn**:  
* The first one displays how many times non-stop words appear in the text (we show only the top 30 in order to improve visualization)
![alice_freq](https://user-images.githubusercontent.com/112963325/197544262-5b4f9208-5977-43a8-9627-a22155363790.png)


* The second histogram represents the probability of each word (for better visualization, we only show words whose probability is greater than 0.3%).
![alice_prob](https://user-images.githubusercontent.com/112963325/197544291-d80e52f0-717a-4c36-86e5-7b23f04059c1.png)





