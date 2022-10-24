# Alice in Wonderland
A simple textual analysis of the text from "Alice in Wonderland" by Lewis Carroll.

The objetive is to analyse how many times non-stop words are present in the text of "Alice in Wonderland".

In order to do so, first we tokenize the text using NLTK.

Then we get remove all the stop-words, as well as punctuation and suffixes.

Now that the data is normalized, we create a frequency dictionary, telling us how many times each word is present in the text.

Then we create a dictionary of probabilities, telling us what is the probability of a word being picked at random from all the non-stop words from the text.

Finally, we create two histograms:  
* The first displays how many times non-stop words appear in the text (be show only the top 30 in order to improve visualization)
![alice_hist_freq](https://user-images.githubusercontent.com/112963325/197467721-d2c5fc23-2a2b-4d35-9357-a3c25aedf865.png)

* The second histogram represents the probability of each word (for better visualization, we only show words whose probability is greater than 0.3%).
![alice_hist_prob](https://user-images.githubusercontent.com/112963325/197467928-4a22f16d-f3ed-4412-a66a-933d578cd864.png)




